#Three Assembly code to x86(AT&T syntax)
import sys
from IR import IR
from parser import parser
from reg import Reg

def isNumeric(strg):
	if strg.isdigit() or (strg[0] is '-' and strg[1:].isdigit()):
		return True
	return False

# check for if the variable is in the memory

def isMem(inp, reglist):
	if inp not in reglist:
		return '(' + inp + ')'
	else:
		return inp

def translate(instruction, leader, ir,register):
	generated_code = ""
	ops = {
		'+' : 'add',
		'-' : 'sub',
		'>>' : 'shr',
		'<<' : 'shl',
		'&&' : 'and',
		'||' : 'or'
	}
	instruction = instruction.split(', ')
	#Disply the three address code in the starting of each. For debuggin
	generated_code += '\n\t'+'#' + ''.join(x+ ', ' for x in instruction) + '\n'
	#ASSIGNMENT OPERATIONS
	if (instruction[1] == '+') or (instruction[1] == '-') or (instruction[1] == '<<') or (instruction[1] == '>>') or (instruction[1] == '&&') \
		 or (instruction[1] == '||') :
		#<line number,operator,destination, arg1, arg2>
		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if(instruction[1] == '+'):
				generated_code +=  "movl $" + str(int(instruction[4])+int(instruction[3])) + ", " + new_place + "\n"
			elif(instruction[1] == '-'):
				generated_code += "movl $" + str(int(instruction[4])-int(instruction[3])) + ", " + new_place + "\n"
			elif(instruction[1] == '<<'):
				generated_code += "movl $" + str(int(instruction[4])<<int(instruction[3])) + ", " + new_place + "\n"
			elif(instruction[1] == '>>'):
				generated_code += "movl $" + str(int(instruction[4])>>int(instruction[3])) + ", " + new_place + "\n"
			elif(instruction[1] == '&&'):
				generated_code += "movl $" + str(int(instruction[4]) and int(instruction[3])) + ", " + new_place + "\n"
			elif(instruction[1] == '||'):
				generated_code += "movl $" + str(int(instruction[4]) or int(instruction[3])) + ", " + new_place + "\n"

		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if instruction[2] != instruction[4]:
				generated_code +="movl " + isMem(ir.address_descriptor[instruction[4]],register.regdict.keys()) + ", " + new_place + "\n"
			generated_code += ops[instruction[1]] + " $" + str(int(instruction[3])) + ", " + new_place + "\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			if(instruction[1]=="<<" or instruction[1]==">>"):
				print("Shifting with non-constants is not valid. Exiting")
				sys.exit()
			ir.address_descriptor, asm  = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if instruction[2] != instruction[3]:
				generated_code += "movl $" + str(int(instruction[4])) + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + new_place + "\n"
			else:
					generated_code += '\t' + "movl " + new_place + ', ' + instruction[2] + "\n"
					generated_code += '\t' + "movl $" + str(int(instruction[4])) + ', ' + new_place + "\n"
					generated_code += ops[instruction[1]] + " (" + instruction[2] + ") , " + new_place + "\n"
					# generated_code += ops[instruction[1]] + " $" + str(int(instruction[4])) + ", " + new_place + "\n"


		else:
			if(instruction[1]=="<<" or instruction[1]==">>"):
				print("Shifting with non-constants is not valid. Exiting")
				sys.exit()


			ir.address_descriptor , asm = register.getReg(ir.next_use_table[leader], instruction, ir.address_descriptor, ir.variable_list)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if instruction[2] != instruction[3] and instruction[2] != instruction[4]:
				generated_code += "movl " + isMem(ir.address_descriptor[instruction[4]], register.regdict.keys()) + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + new_place + "\n"
			else:
				if instruction[2] == instruction[3]:
					generated_code += '\t' + "movl " + new_place + ', ' + instruction[2] + "\n"
					generated_code += '\t' + "movl " + isMem(ir.address_descriptor[instruction[4]],register.regdict.keys()) + ', ' + new_place + "\n"
					generated_code += ops[instruction[1]] + " (" + instruction[2] + ") , " + new_place + "\n"
				elif instruction[2] == instruction[4]:
					# if(isMem(ir.address_descriptor[instruction[4]],register.regdict.keys())[0] == '('):
					generated_code += ops[instruction[1]] + " " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + new_place + "\n"


# # ---------------------------------------------------------------------------------------
	elif instruction[1] == '==':
		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			generated_code +=  "movl $" + str(int(instruction[4]) == int(instruction[3])) + ", " + new_place + "\n"
			
		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if instruction[2] != instruction[4]:
				generated_code +="movl " + isMem(ir.address_descriptor[instruction[4]],register.regdict.keys()) + ", " + new_place + "\n"
			generated_code += ops[instruction[1]] + " $" + str(int(instruction[3])) + ", " + new_place + "\n"


	elif instruction[1] == '*':
		#<line number,operator,destination, arg1, arg2>

		regs = ['%eax','%edx']
		for reg in regs:
			var = register.regdict[reg]
			#If the register is in use
			if(len(var)):
				generated_code += '\t' + "movl " + reg + ", " + var + "\n"
				ir.address_descriptor[var] = var
				register.regdict[reg] = ""

		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			generated_code += '\t' + "movl $" + str(int(instruction[3])*int(instruction[4])) + ", " + "%edx" + "\n"

		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			generated_code += '\t' +"movl $" + str(int(instruction[3])) + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[4]] + ", " + "%edx" + "\n"
			generated_code += '\t' + "imul %edx\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			generated_code += '\t' +"movl $" + str(int(instruction[4])) + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + "%edx" + "\n"
			generated_code += '\t' + "imul %edx\n"

		else:
			generated_code += '\t' +"movl " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl " + isMem(ir.address_descriptor[instruction[4]],register.regdict.keys()) + ", " + "%edx" + "\n"
			generated_code += '\t' + "imul %edx\n"

		ir.address_descriptor[instruction[2]] = "%eax"
		for regs in register.regdict.keys():
			if register.regdict[regs] == instruction[2]:
				register.regdict[regs] = ''
		register.regdict["%eax"] = instruction[2]

# ---------------------------------------------------------------------------------------
	elif instruction[1] == '/' or instruction[1] == '%' :
		#<line number,operator,destination, arg1, arg2>
		#Divide EDX(0):EAX(arg1) by arg2 and quotient in EAX and the remainder in EDX.
		regs = ['%eax','%edx','%ecx']
		for reg in regs:
			var = register.regdict[reg]
			if(len(var)):
				generated_code += '\t' + "movl " + reg + ", " + var + "\n"
				ir.address_descriptor[var] = var
				register.regdict[reg] = ""

		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			if instruction[1] == '/' :
				generated_code += '\t' + "movl $" + str(int(instruction[4]) / int(instruction[3])) + ", " + "%eax" + "\n"
			else:
				generated_code += '\t' + "movl $" + str(int(instruction[4]) % int(instruction[3])) + ", " + "%edx" + "\n"

		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			generated_code += '\t' + "movl $0, %edx" + "\n"
			generated_code += '\t' +"movl " + isMem(ir.address_descriptor[instruction[4]],register.regdict.keys()) + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl $" + str(int(instruction[3])) + ", " + "%ecx" + "\n"
			# register.regdict["%ecx"] = instruction[4]
			generated_code += '\t' + "idiv %ecx\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			generated_code += '\t' + "movl $0, %edx" + "\n"
			generated_code += '\t' +"movl $" + str(int(instruction[4])) + ", " + "%eax" + "\n"
			# register.regdict["%eax"] = instruction[3]
			generated_code += '\t' +"movl " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + "%ecx" + "\n"
			generated_code += '\t' + "idiv %ecx\n"

		else:
			generated_code += '\t' + "movl $0, %edx" + "\n"
			generated_code += '\t' +"movl " + isMem(ir.address_descriptor[instruction[4]],register.regdict.keys()) + ", " + "%eax" + "\n"
			# register.regdict["%eax"] = instruction[3]
			generated_code += '\t' +"movl " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + "%ecx" + "\n"
			# register.regdict["%ecx"] = instruction[4]
			generated_code += '\t' + "idiv %ecx\n"

		if instruction[1] == '/':
			ir.address_descriptor[instruction[2]] = "%eax"
			for regs in register.regdict.keys():
				if register.regdict[regs] == instruction[2]:
					register.regdict[regs] = ''
			register.regdict["%eax"] = instruction[2]
		else:
			ir.address_descriptor[instruction[2]] = "%edx"
			for regs in register.regdict.keys():
				if register.regdict[regs] == instruction[2]:
					register.regdict[regs] = ''
			register.regdict["%edx"] = instruction[2]

# ---------------------------------------------------------------------------------------

	elif instruction[1] == "~" or instruction[1] == "=" :

		if instruction[3] ==  'arr_init':
			print("############################33333")
			# pass
		else:
			if isNumeric(instruction[3]):
				ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
				generated_code += '\t' + asm
				new_place = ir.address_descriptor[instruction[2]]
				if(instruction[1] == '~'):
					generated_code += "movl $" + str(not int(instruction[3])) + ", " + new_place + "\n"
				else :
					generated_code += "movl $" + str(int(instruction[3])) + ", " + new_place + "\n"
			else:
				ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
				generated_code += '\t' + asm
				new_place = ir.address_descriptor[instruction[2]]
				# generated_code += "movl " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"
				if(ir.address_descriptor[instruction[3]] is not new_place):
					generated_code += "movl " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + new_place + "\n"
				# else:
					# generated_code += "movl " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"
				if(instruction[1] == '~'):
					generated_code += "notl " + new_place + "\n"

			# register.regdict["%edx"] = ""
			# ir.address_descriptor[instruction[2]] = ""
	elif instruction[1] == 'array_asgn':
		# ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list,var=instruction[2])
		# idx = asm.find(instruction[2])
		# asm = list(asm)
		# asm[idx-1] = '$'
		# asm[idx+len(instruction[2])] = ''
		# asm = "".join(asm)
		# generated_code += '\t' + asm

		# # print(ir.address_descriptor)
		# # print(register.regdict)
		# new_place = ir.address_descriptor[instruction[2]]
		# generated_code += "add $" + instruction[3] + " ," + new_place + '\n'
		# if isNumeric(instruction[4]):
		# 	generated_code += "movl $" + instruction[4] + ", (" + new_place + ')' + "\n"
		# else:
		# 	# reg = 
		# 	# if reg[0]=='%':
		# 	# else:
		# 	ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list,var=instruction[4])
		# 	generated_code += '\t' + asm
		# 	generated_code += "movl " + ir.address_descriptor[instruction[4]] + ", (" + new_place + ')' + "\n"
		# 	# if(ir.address_descriptor[instruction[3]] is not new_place):
		# 		# generated_code += "movl " + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + ", " + new_place + "\n"
		if isNumeric(instruction[4]):
			generated_code += "movl $" + instruction[4] + ", (" + instruction[2] + '+' + instruction[3] + ')' + "\n"
		else:

			ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list,var=instruction[4])
			generated_code += '\t' + asm
			generated_code += "movl " + ir.address_descriptor[instruction[4]] + ", (" + instruction[2] + '+' + instruction[3] + ')' + "\n"

	elif instruction[1] == 'array_access':
		ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list,var=instruction[2])
		generated_code += '\t' + asm
		generated_code += "movl " + "(" + instruction[3] + '+' + instruction[4] + '), ' + ir.address_descriptor[instruction[2]] + "\n"


# ------------------------------------------------------------------------------------------------------------
	elif instruction[1] == 'label':
		#<line number, label, label>
		generated_code += instruction[-1] + ": \n"

	# if instruction[1] == 'if':
	# 	#Syntax <line number,operator,condition_op,arg1,arg2,line_no>
	# 	#lt , gt , leq, geq, ne, eq

	elif instruction[1] == 'goto':
		#Syntax <line_number, goto, label>
		generated_code += '\t' + "jmp " + instruction[2] + "\n"

	elif instruction[1] == 'conditional_goto':
		if isNumeric(instruction[-2]) and isNumeric(instruction[3]):
			generated_code += 'cmp $' + instruction[-2] + ', $' + instruction[3] + '\n'
		elif not isNumeric(instruction[-2]):
			if instruction[-2] in register.regdict.values():
				generated_code += '\t' + 'cmp ' + isMem(ir.address_descriptor[instruction[-2]],register.regdict.keys()) + ' , ' + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) +'\n'
			else:

				ir.address_descriptor, asm = register.getRegister(instruction[-2], ir.address_descriptor, ir.next_use_table[leader], int(instruction[0]))
				generated_code += '\t' + asm
				generated_code += '\t' + 'cmp ' + isMem(ir.address_descriptor[instruction[-2]],register.regdict.keys()) + ' , ' + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + '\n'
		else:
			if instruction[3] in register.regdict.values():
				generated_code += '\t' + 'cmp $' + instruction[-2] + ' , ' + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + '\n'
			else:
				ir.address_descriptor, asm = register.getRegister(instruction[3], ir.address_descriptor, ir.next_use_table[leader], int(instruction[0]))
				generated_code += '\t' + asm
				generated_code += '\t' + 'cmp $' + instruction[-2] + ' , ' + isMem(ir.address_descriptor[instruction[3]],register.regdict.keys()) + '\n'

		if instruction[2] == 'leq':
			generated_code += '\t' + 'jle '
		if instruction[2] == 'le':
			generated_code += '\t' + 'jl '
		if instruction[2] == 'geq':
			generated_code += '\t' + 'jge '
		if instruction[2] == 'ge':
			generated_code += '\t' + 'jg '
		if instruction[2] == '==':
			generated_code += '\t' + 'je '
		if instruction[2] == '~':
			generated_code += '\t' + 'jne '

		generated_code += instruction[-1] + '\n'

	elif instruction[1] == 'fn_call_1':
		arg_num = instruction[3]
		# iterate over the parameters
		for i in range(int(arg_num)):
			param = instruction[4+i]
			if isNumeric(param):
				param = "$" + param
			else:
				param = isMem(ir.address_descriptor[param],register.regdict.keys())
			generated_code += '\t'+ 'pushl ' + param + '\n'
		
		generated_code += '\t' + 'call ' + instruction[2] + '\n'

	elif instruction[1] == 'fn_call_2':
		arg_num = instruction[3]
		# iterate over the parameters
		for i in range(int(arg_num)):
			param = instruction[4+i]
			if isNumeric(param):
				param = "$" + param
			else:
				param = isMem(ir.address_descriptor[param],register.regdict.keys())
			generated_code += '\t'+ 'pushl ' + param + '\n'
		
		generated_code += '\t' + 'call ' + instruction[2] + '\n'
		generated_code += 'movl %eax, ' + instruction[-1] + '\n'
		ir.address_descriptor[instruction[-1]] = '%eax'
		register.regdict['%eax'] = instruction[-1]

	elif instruction[1] == 'fn_def':
		generated_code += instruction[2] + ':\n'
		generated_code += '\t' + 'pushl %ebp\n'
		generated_code += '\t' + 'movl %esp, %ebp\n'

		arg_num = instruction[3]
		# iterate over the parameters
		for i in range(int(arg_num)):
			param = instruction[4+i]
			displacement = 4*(int(arg_num) - i)
			if ir.address_descriptor[param] not in register.regdict.keys():
				ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list, param)
			generated_code += asm
			temp = ir.address_descriptor[param]
			# generated_code += '\t' + 'movl '+ str(displacement) + '(%ebp)' + ', ' + isMem(ir.address_descriptor[param], register.regdict.keys()) + '\n'
			generated_code += '\t' + 'movl '+ str(displacement) + '(%ebp)' + ', ' + temp + '\n'
			generated_code += '\t' + 'movl ' + temp + ', ' + param + '\n'
		
		# generated_code += "### Flushing -----------\n"
		# for reg,var in register.regdict.items():
		# 	if var is not "":
		# 		generated_code += '\t' + "movl " + reg + ", " + var + "\n"
		# 		register.regdict[reg] = ""
		# 		ir.address_descriptor[var] = var
		# generated_code+= "### Flushed ------------\n"

	elif instruction[1] == 'return':
		if(leader==1):
			generated_code += '\t' + 'call exit\n'

		elif len(instruction) is 2:
			generated_code += '\t' + 'leave\n'
			generated_code += '\t' + 'ret\n'

		else:
			var = instruction[-1]
			generated_code += '\t' + 'movl ' + isMem(ir.address_descriptor[instruction[-1]], register.regdict.keys()) + ', %eax\n'

			generated_code += '\t' + 'leave\n'
			generated_code += '\t' + 'ret\n'

	# elif instruction[1] == 'return':

	elif instruction[1] == 'print':

# -------------- Flushing
		generated_code += "### Flushing -----------\n"
		for reg,var in register.regdict.items():
			if var is not "":
				generated_code += '\t' + "movl " + reg + ", " + var + "\n"
				register.regdict[reg] = ""
				ir.address_descriptor[var] = var
		generated_code+= "### Flushed ------------\n"

		if isNumeric(instruction[2]):

			generated_code+= '\t'+ "pushl $" + str(instruction[2]) + "\n"
			generated_code += '\t'+ "pushl $format1\n"
			generated_code += '\t'+ "call printf\n"

		else:
			if( isMem(ir.address_descriptor[instruction[2]],register.regdict.keys())[0] is not '('):
				generated_code+= '\t'+ "movl " + ir.address_descriptor[instruction[2]] + "," + instruction[2] + "\n"
				generated_code+= '\t'+ "pushl " + ir.address_descriptor[instruction[2]] + "\n"
				generated_code += '\t'+ "pushl $format1\n"
				generated_code += '\t'+ "call printf\n"
				generated_code+= '\t'+ "movl " + '(' + instruction[2] + ")," + ir.address_descriptor[instruction[2]] + "\n"
				register.regdict[ir.address_descriptor[instruction[2]]] = instruction[2]
			else:
				generated_code+= '\t'+ "pushl " + ir.address_descriptor[instruction[2]] + "\n"
				generated_code += '\t'+ "pushl $format1\n"
				generated_code += '\t'+ "call printf\n"
	
	elif instruction[1] == 'print_char':

# -------------- Flushing
		generated_code += "### Flushing -----------\n"
		for reg,var in register.regdict.items():
			if var is not "":
				generated_code += '\t' + "movl " + reg + ", " + var + "\n"
				register.regdict[reg] = ""
				ir.address_descriptor[var] = var
		generated_code+= "### Flushed ------------\n"

		if isNumeric(instruction[2]):

			generated_code+= '\t'+ "pushl $" + str(instruction[2]) + "\n"
			generated_code += '\t'+ "pushl $format2\n"
			generated_code += '\t'+ "call printf\n"

		else:
			if( isMem(ir.address_descriptor[instruction[2]],register.regdict.keys())[0] is not '('):
				generated_code+= '\t'+ "movl " + ir.address_descriptor[instruction[2]] + "," + instruction[2] + "\n"
				generated_code+= '\t'+ "pushl " + ir.address_descriptor[instruction[2]] + "\n"
				generated_code += '\t'+ "pushl $format2\n"
				generated_code += '\t'+ "call printf\n"
				generated_code+= '\t'+ "movl " + '(' + instruction[2] + ")," + ir.address_descriptor[instruction[2]] + "\n"
				register.regdict[ir.address_descriptor[instruction[2]]] = instruction[2]
			else:
				generated_code+= '\t'+ "pushl " + ir.address_descriptor[instruction[2]] + "\n"
				generated_code += '\t'+ "pushl $format2\n"
				generated_code += '\t'+ "call printf\n"

	elif instruction[1] == 'scan':

# -------------- Flushing
		generated_code += "### Flushing -----------\n"
		for reg,var in register.regdict.items():
			if var is not "":
				generated_code += '\t' + "movl " + reg + ", " + var + "\n"
				register.regdict[reg] = ""
				ir.address_descriptor[var] = var
		generated_code+= "### Flushed ------------\n"

		var = instruction[-1]
		generated_code += 'pushl $' + var + '\n'
		generated_code += 'pushl $format\n'
		generated_code += 'call scanf\n'

	elif instruction[1] == 'exit':
		generated_code += '\t'+ 'call exit\n'



	return generated_code,ir,register

import sys
from IR import IR
from parser import parser
from reg import Reg

def isNumeric(strg):
	if strg.isdigit() or (strg[0] is '-' and strg[1:].isdigit()):
		return True
	return False

# check for if the variable is in the memory



def translate(instruction, leader, ir,register):
	generated_code = ""
	ops = {
		'+' : 'add',
		'-' : 'sub',
		'>>' : 'shr',
		'<<' : 'shl',
		'&&' : 'and',
		'||' : 'or',
		'<'  : 'cmp',
		'>'	 : 'cmp',
		'<=' : 'cmp',
		'>=' : 'cmp',
		'==' : 'cmp',
		'~=' : 'cmp'
	}
	instruction = instruction.split(', ')
	#Disply the three address code in the starting of each. For debuggin
	generated_code += '\n\t'+'#' + ''.join(x+ ', ' for x in instruction) + '\n'
	#ASSIGNMENT OPERATIONS
	#TODO Add support for < , > <=, >=, ==, ~= . Soumye will do
	if (instruction[1] == '+') or (instruction[1] == '-') or (instruction[1] == '<<') or (instruction[1] == '>>') or (instruction[1] == '&&') \
		 or (instruction[1] == '||') or instruction[1] == '<' or instruction[1] == '>' or instruction[1] == '<=' or instruction[1] == '>=' \
		 or instruction[1] == '==' or instruction[1] == '~=' :
		#<line number,operator,destination, arg1, arg2>
		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if(instruction[1] == '+'):
				generated_code +=  "movl $" + str(int(instruction[3])+int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '-'):
				generated_code += "movl $" + str(int(instruction[3])-int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '<<'):
				generated_code += "movl $" + str(int(instruction[3])<<int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '>>'):
				generated_code += "movl $" + str(int(instruction[3])>>int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '&&'):
				generated_code += "movl $" + str(int(instruction[3]) and int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '||'):
				generated_code += "movl $" + str(int(instruction[3]) or int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '<'):
				generated_code += "movl $" + str(int(int(instruction[3]) < int(instruction[4]))) + ", " + new_place + "\n"
			elif(instruction[1] == '>'):
				generated_code += "movl $" + str(int(int(instruction[3]) > int(instruction[4]))) + ", " + new_place + "\n"
			elif(instruction[1] == '<='):
				generated_code += "movl $" + str(int(int(instruction[3]) <= int(instruction[4]))) + ", " + new_place + "\n"
			elif(instruction[1] == '>='):
				generated_code += "movl $" + str(int(int(instruction[3]) >= int(instruction[4]))) + ", " + new_place + "\n"
			elif(instruction[1] == '=='):
				generated_code += "movl $" + str(int(int(instruction[3]) == int(instruction[4]))) + ", " + new_place + "\n"
			elif(instruction[1] == '~='):
				generated_code += "movl $" + str(int(int(instruction[3]) != int(instruction[4]))) + ", " + new_place + "\n"
			

		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			ir.address_descriptor, asm = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if(new_place==ir.address_descriptor[instruction[4]]):
				generated_code += ops[instruction[1]] + " $" + str(int(instruction[3])) + ", " + new_place + "\n"
			else:
				generated_code +="movl $" + str(int(instruction[3])) + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor, asm  = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if(new_place==ir.address_descriptor[instruction[3]]):
				generated_code += ops[instruction[1]] + " $" + str(int(instruction[4])) + ", " + new_place + "\n"
			else:
				generated_code += "movl $" + str(int(instruction[4])) + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"

		else:
			ir.address_descriptor , asm = register.getReg(ir.next_use_table[leader], instruction, ir.address_descriptor, ir.variable_list)
			generated_code += '\t' + asm
			new_place = ir.address_descriptor[instruction[2]]
			if(new_place==ir.address_descriptor[instruction[3]]):
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"
			elif(new_place==ir.address_descriptor[instruction[4]]):
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"
			else:
				generated_code += "movl " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"

# # --------------------------------------------------------------------------------------- 

	elif instruction[1] == '*':
		#<line number,operator,destination, arg1, arg2>
		regs = ['%eax','%edx']
		for reg in regs:
			var = register.regdict[reg]
			#If the register is in use
			if(len(var)):
				generated_code += '\t' + "movl " + reg + ", $" + var + "\n"
				ir.address_descriptor[var] = "$" + var

		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			generated_code += '\t' + "movl $" + str(int(instruction[3])*int(instruction[4])) + ", " + "%edx" + "\n"
		
		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			generated_code += '\t' +"movl $" + str(int(instruction[3])) + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[4]] + ", " + "%edx" + "\n"
			generated_code += '\t' + "imul %edx\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			generated_code += '\t' +"movl $" + str(int(instruction[4])) + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[3]] + ", " + "%edx" + "\n"
			generated_code += '\t' + "imul %edx\n"

		else:
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[3]] + ", " + "%eax" + "\n"
			# print(instruction[4])
			# print(ir.address_descriptor[instruction[4]])
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[4]] + ", " + "%edx" + "\n"
			generated_code += '\t' + "imul %edx\n"

		ir.address_descriptor[instruction[2]] = "%edx"

# --------------------------------------------------------------------------------------- 
	elif instruction[1] == '/' or instruction[1] == '%' :
		#<line number,operator,destination, arg1, arg2>
		#Divide EDX(0):EAX(arg1) by arg2 and quotient in EAX and the remainder in EDX.
		regs = ['%eax','%edx','%ecx']
		for reg in regs:
			var = register.regdict[reg]
			if(len(var)):
				generated_code += '\t' + "movl " + reg + ", $" + var + "\n"
				ir.address_descriptor[var] = "$" + var

		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			if instruction[1] == '/' :
				generated_code += '\t' + "movl $" + str(int(instruction[3]) / int(instruction[4])) + ", " + "%eax" + "\n"
			else:
				generated_code += '\t' + "movl $" + str(int(instruction[3]) % int(instruction[4])) + ", " + "%edx" + "\n"

		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			generated_code += '\t' + "movl $0, %edx" + "\n"
			generated_code += '\t' +"movl $" + str(int(instruction[3])) + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[4]] + ", " + "%ecx" + "\n"
			generated_code += '\t' + "idiv %ecx\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			generated_code += '\t' + "movl $0, %edx" + "\n"
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[3]] + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl $" + str(int(instruction[4])) + ", " + "%ecx" + "\n"
			generated_code += '\t' + "idiv %ecx\n"

		else:
			generated_code += '\t' + "movl $0, %edx" + "\n"
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[3]] + ", " + "%eax" + "\n"
			generated_code += '\t' +"movl " + ir.address_descriptor[instruction[4]] + ", " + "%ecx" + "\n"
			generated_code += '\t' + "idiv %ecx\n"

		if instruction[1] == '/':
			ir.address_descriptor[instruction[2]] = "%eax"
		else:
			ir.address_descriptor[instruction[2]] = "%edx"

# --------------------------------------------------------------------------------------- 

	elif instruction[1] == "~" or instruction[1] == "=" :
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
				generated_code += "movl " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"
			# else:
				# generated_code += "movl " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"
			if(instruction[1] == '~'):
				generated_code += "notl " + new_place + "\n"


# ------------------------------------------------------------------------------------------------------------
	elif instruction[1] == 'label':
		#<line number, label, label>
		generated_code += instruction[-1] + ": \n"

	# if instruction[1] == 'if':
	# 	#Syntax <line number,operator,condition_op,arg1,arg2,line_no>	
	# 	#lt , gt , leq, geq, ne, eq

	elif instruction[1] == 'goto':
		#Syntax <line_number, goto, label>
		generated_code += '\t' + "jmp" + instruction[2] + "\n"

	elif instruction[1] == 'conditional_goto':
		if not isNumeric(instruction[-2]):
			if instruction[-2] in register.regdict.values():
				generated_code += '\t' + 'cmp ' + ir.address_descriptor[instruction[-2]] + ' , ' + ir.address_descriptor[instruction[3]] +'\n'
			else:
				ir.address_descriptor , asm = register.getRegister(instruction[-2], ir.address_descriptor, ir.next_use_table[leader], int(instruction[0]))
				generated_code += '\t' + asm
				generated_code += '\t' + 'cmp ' + ir.address_descriptor[instruction[-2]] + ' , ' + ir.address_descriptor[instruction[3]] + '\n'
		else:
			if instruction[3] in register.regdict.values():
				generated_code += '\t' + 'cmp $' + instruction[-2] + ' , ' + ir.address_descriptor[instruction[3]] + '\n'
				# print(ir.address_descriptor)
			else:
				ir.address_descriptor , asm = register.getRegister(instruction[-2], ir.address_descriptor, ir.next_use_table[leader], int(instruction[0]))
				generated_code += '\t' + asm
				generated_code += '\t' + 'cmp $' + instruction[-2] + ' , ' + ir.address_descriptor[instruction[3]] + '\n'

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

	elif instruction[1] == 'fn_call_1': # TODO: Flush reg. and save all to mem before and after
		generated_code += '\t' + 'call ' + instruction[2] + '\n'

	elif instruction[1] == 'fn_call_2': # TODO: Flush reg. and save all to mem before and after
		generated_code += '\t' + 'call ' + instruction[2] + '\n'
		ir.address_descriptor[instruction[-1]] = '%eax'
		register.regdict['%eax'] = instruction[-1]

	elif instruction[1] == 'fn_def': # TODO: Flush reg. and save all to mem before and after
		generated_code += instruction[-1] + ':\n'

	elif instruction[1] == 'return':
		if len(instruction) is 2:
			generated_code += '\t' + 'leave\n'
			generated_code += '\t' + 'ret\n'
		else:
			var = instruction[-1]
			# TODO: Save and flush all registers

	elif instruction[1] == 'print':

		if isNumeric(instruction[2]):

			generated_code+= '\t'+ "pushl $" + str(instruction[2]) + "\n"
			# generated_code += '\t'+ "pushl $str\n"
			generated_code += '\t'+ "call printf\n"

		else:
			generated_code+= '\t'+ "pushl " + ir.address_descriptor[instruction[2]] + "\n"
			generated_code += '\t'+ "pushl $format\n"
			generated_code += '\t'+ "call printf\n"

	elif instruction[1] == '\t'+ 'exit':
		generated_code += '\t'+ 'call exit\n'

	# elif operator == "print":
	# 	operand = instruction[2]
	# 	if not isnumber(operand):
	# 		loc = getlocation(operand)
	# 		if not loc == "mem":
	# 			assembly = assembly + "pushl " + loc + "\n"
	# 			assembly = assembly + "pushl $str\n"
	# 			assembly = assembly + "call printf\n"
	# 		else:
	# 			assembly = assembly + "pushl " + operand + "\n"
	# 			assembly = assembly + "pushl $str\n"
	# 			assembly = assembly + "call printf\n"
	# 	else:
	# 		assembly = assembly + "pushl $" + operand + "\n"
	# 		assembly = assembly + "pushl $str\n"
	# 		assembly = assembly + "call printf\n"			



	return generated_code,ir,register;
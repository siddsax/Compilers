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
		'||' : 'or'
	}
	instruction = instruction.split(', ')
	print(instruction[0])
	if (instruction[1] == '+') or (instruction[1] == '-') or (instruction[1] == '<<') or (instruction[1] == '>>') or (instruction[1] == '&&') or (instruction[1] == '||') :
		#<line number,operator,destination, arg1, arg2>
		print("shit+")
		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor)
			new_place = ir.address_descriptor[instruction[2]]
			if(instruction[1] == '+'):
				generated_code += "mov $" + str(int(instruction[3])+int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '<<'):
				generated_code += "mov $" + str(int(instruction[3])<<int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '>>'):
				generated_code += "mov $" + str(int(instruction[3])>>int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '&&'):
				generated_code += "mov $" + str(int(instruction[3]) and int(instruction[4])) + ", " + new_place + "\n"
			elif(instruction[1] == '||'):
				generated_code += "mov $" + str(int(instruction[3]) or int(instruction[4])) + ", " + new_place + "\n"
			else:
				generated_code += "mov $" + str(int(instruction[3])-int(instruction[4])) + ", " + new_place + "\n"

		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			new_place = ir.address_descriptor[instruction[2]]
			if(new_place==ir.address_descriptor[instruction[4]]):
				generated_code += ops[instruction[1]] + " $" + str(int(instruction[3])) + ", " + new_place + "\n"
			else:
				generated_code +="mov $" + str(int(instruction[3])) + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			new_place = ir.address_descriptor[instruction[2]]
			if(new_place==ir.address_descriptor[instruction[3]]):
				generated_code += ops[instruction[1]] + " $" + str(int(instruction[4])) + ", " + new_place + "\n"
			else:
				generated_code += "mov $" + str(int(instruction[4])) + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"

		else:
			ir.address_descriptor = register.getReg(ir.next_use_table[leader], instruction, ir.address_descriptor, ir.variable_list)
			new_place = ir.address_descriptor[instruction[2]]
			if(new_place==ir.address_descriptor[instruction[3]]):
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"
			elif(new_place==ir.address_descriptor[instruction[4]]):
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"
			else:
				generated_code += "mov " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"
				generated_code += ops[instruction[1]] + " " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"

# # --------------------------------------------------------------------------------------- 

	elif instruction[1] == '*':
		#<line number,operator,destination, arg1, arg2>
		print("shit*")
		regs = ['%eax','%edx']
		for reg in regs:
			var = register.regdict[reg]
			#If the register is in use
			if(len(var)):
				generated_code += "mov " + reg + ", $" + var + "\n"
				ir.address_descriptor[var] = "$" + var

		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			generated_code += "mov $" + str(int(instruction[3])*int(instruction[4])) + ", " + "%edx" + "\n"
		
		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code +="mov $" + str(int(instruction[3])) + ", " + "%eax" + "\n"
			generated_code +="mov " + ir.address_descriptor[instruction[4]] + ", " + "%edx" + "\n"
			generated_code += "imul %edx\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code +="mov $" + str(int(instruction[4])) + ", " + "%eax" + "\n"
			generated_code +="mov " + ir.address_descriptor[instruction[3]] + ", " + "%edx" + "\n"
			generated_code += "imul %edx\n"

		else:
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code +="mov " + ir.address_descriptor[instruction[3]] + ", " + "%eax" + "\n"
			print(instruction[4])
			print(ir.address_descriptor[instruction[4]])
			generated_code +="mov " + ir.address_descriptor[instruction[4]] + ", " + "%edx" + "\n"
			generated_code += "imul %edx\n"

		ir.address_descriptor[instruction[2]] = "%edx"

# --------------------------------------------------------------------------------------- 
	elif instruction[1] == '/' or instruction[1] == '%' :
		#<line number,operator,destination, arg1, arg2>
		#Divide EDX(0):EAX(arg1) by arg2 and quotient in EAX and the remainder in EDX.
		regs = ['%eax','%edx','%ecx']
		for reg in regs:
			var = register.regdict[reg]
			if(len(var)):
				generated_code += "mov " + reg + ", $" + var + "\n"
				ir.address_descriptor[var] = "$" + var

		if isNumeric(instruction[3]) and isNumeric(instruction[4]):
			if instruction[1] == '/' :
				generated_code += "mov $" + str(int(instruction[3]) / int(instruction[4])) + ", " + "%eax" + "\n"
			else:
				generated_code += "mov $" + str(int(instruction[3]) % int(instruction[4])) + ", " + "%edx" + "\n"

		elif isNumeric(instruction[3]) and not isNumeric(instruction[4]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += "mov $0, %edx" + "\n"
			generated_code +="mov $" + str(int(instruction[3])) + ", " + "%eax" + "\n"
			generated_code +="mov " + ir.address_descriptor[instruction[4]] + ", " + "%ecx" + "\n"
			generated_code += "idiv %ecx\n"

		elif not isNumeric(instruction[3]) and isNumeric(instruction[4]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += "mov $0, %edx" + "\n"
			generated_code +="mov " + ir.address_descriptor[instruction[3]] + ", " + "%eax" + "\n"
			generated_code +="mov $" + str(int(instruction[4])) + ", " + "%ecx" + "\n"
			generated_code += "idiv %ecx\n"

		else:
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			generated_code += "mov $0, %edx" + "\n"
			generated_code +="mov " + ir.address_descriptor[instruction[3]] + ", " + "%eax" + "\n"
			generated_code +="mov " + ir.address_descriptor[instruction[4]] + ", " + "%ecx" + "\n"
			generated_code += "idiv %ecx\n"

		if instruction[1] == '/':
			ir.address_descriptor[instruction[2]] = "%eax"
		else:
			ir.address_descriptor[instruction[2]] = "%edx"

# --------------------------------------------------------------------------------------- 

	elif instruction[1] == "~" or instruction[1] == "=" :
		print("shit~")
		if isNumeric(instruction[3]):
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			new_place = ir.address_descriptor[instruction[2]]
			if(instruction[1] == '~'):
				generated_code += "mov $" + str(not int(instruction[3])) + ", " + new_place + "\n"
			else :
				generated_code += "mov $" + str(int(instruction[3])) + ", " + new_place + "\n"
		else:
			ir.address_descriptor = register.getReg(ir.next_use_table[leader],instruction,ir.address_descriptor, ir.variable_list)
			new_place = ir.address_descriptor[instruction[2]]
			# generated_code += "mov " + ir.address_descriptor[instruction[4]] + ", " + new_place + "\n"
			if(ir.address_descriptor[instruction[3]] is not new_place):
				generated_code += "mov " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"
			# else:
				# generated_code += "mov " + ir.address_descriptor[instruction[3]] + ", " + new_place + "\n"
			if(instruction[1] == '~'):
				generated_code += "notl " + new_place + "\n"
	
# ------------------------------------------------------------------------------------------------------------
	# if instruction[1] == 'label':
	# 	#<line number, label, label>
	# 	generated_code += instruction[3] + "\n"

	# if instruction[1] == 'if':
	# 	#Syntax <line number,operator,condition_op,arg1,arg2,line_no>	
	# 	#lt , gt , leq, geq, ne, eq

	# if instruction[1] == 'goto':
	# 	#Syntax <line_number, goto, label>
	# 	generated_code += "jmp" + instruction[3] + "\n"

	return generated_code,ir,register;


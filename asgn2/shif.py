import sys 
def translate(instruction):
	assembly = ""
	line = int(instruction[0])
	# assembly = assembly + str(line) + "\n"
	operator = instruction[1]
	# Generating assembly code if the tac is a mathematical operation
	if operator in mathops:

	elif operator == "param":
		#LineNo, param, val
		val = instruction[2]
		if isnumber(val):
			val = "$" + val
		else:
			loc2 = getlocation(val)
			if loc2 != "mem":
				val = addressDescriptor[val]
		assembly = assembly + "pushl " + val + "\n"


	# Generating assembly code if the tac is a function call
	elif operator == "call":
		#Lno., call, func_name, arg_num, ret
		# Add code to write all the variables to the memory
		arg_num = instruction[3]
		for var in varlist:
			loc = getlocation(var)
			if loc != "mem":
				assembly = assembly + "movl " + loc + ", " + var + "\n"
				setlocation(var, "mem")
		label = instruction[2]
		assembly = assembly + "call " + label + "\n"

	# Generating assembly code if the tac is a label for a new leader
	elif operator == "label":
		label = instruction[2]
		assembly = assembly + label + ": \n"

	# Generating assembly code if the tac is an ifgoto statement
	elif operator == "ifgoto":
		# Add code to write all the variables to the memory
		for var in varlist:
			loc = getlocation(var)
			if loc != "mem":
				assembly = assembly + "movl " + loc + ", " + var + "\n"
				setlocation(var, "mem")
		operator = instruction[2]
		operand1 = instruction[3]
		operand2 = instruction[4]
		label = instruction[5]
		#check whether the operands are variables or constants
		if not isnumber(operand1) and not isnumber(operand2): #both the operands are variables
			#Get the locations of the operands
			loc1 = getlocation(operand1)
			loc2 = getlocation(operand2)
			#Get the register for comparing the operands
			reg1 = getReg(operand1, line)
			#generating assembly instructions
			if loc1 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + reg1 + "\n"
			else:
				assembly = assembly + "movl " + operand1 + ", " + reg1 + "\n"
			if loc2 != "mem":
				assembly = assembly + "cmp " + loc2 + ", " + reg1 + "\n"
			else:
				assembly = assembly + "cmp " + operand2 + ", " + reg1 + "\n"
			#updating the registor & address descriptors
			setregister(reg1, operand1)
			setlocation(operand1, reg1)

		elif not isnumber(operand1) and isnumber(operand2): #only operand1 is variables
			#Get the location of the 1st operand
			loc1 = getlocation(operand1)
			if loc1 != "mem":
				assembly = assembly + "cmp $" + operand2 + ", " + loc1 + "\n"
			else:
				assembly = assembly + "cmp $" + operand2 + ", " + operand1 + "\n"
		elif isnumber(operand1) and not isnumber(operand2): #only operand2 is variables
			#Get the location of the 1st operand
			loc2 = getlocation(operand2)
			if loc2 != "mem":
				assembly = assembly + "cmp " + loc2 + ", $" + operand1 + "\n"
			else:
				assembly = assembly + "cmp " + operand2 + ", $" + operand1 + "\n"
		elif isnumber(operand1) and isnumber(operand2): #none of the operandsare variables
			#generate assembly instructions
			assembly = assembly + "cmp $" + operand2 + ", $" + operand1 + "\n"

		# Add code to write all the variables to the memory
		for var in varlist:
			loc = getlocation(var)
			if loc != "mem":
				assembly = assembly + "movl " + loc + ", " + var + "\n"
				setlocation(var, "mem")
		if isnumber(label):
			label = "L" + label
		if operator == "<=":
			assembly = assembly + "jle " + label + "\n"
		elif operator == ">=":
			assembly = assembly + "jge " + label + "\n" 
		elif operator == "==":
			assembly = assembly + "je " + label + "\n" 
		elif operator == "<":
			assembly = assembly + "jl " + label + "\n" 
		elif operator == ">":
			assembly = assembly + "jg " + label + "\n" 
		elif operator == "!=":
			assembly = assembly + "jne " + label + "\n"

	# Generating assembly code if the tac is a goto statement
	elif operator == "goto":
		# Add code to write all the variables to the memory
		for var in varlist:
			loc = getlocation(var)
			if loc != "mem":
				assembly = assembly + "movl " + loc + ", " + var + "\n"
				setlocation(var, "mem")
		
		label = instruction[2]
		if isnumber(label):
			assembly = assembly + "jmp L" + label + "\n"
		else:
			assembly = assembly + "jmp " + label + "\n"

	# Generating assembly code if the tac is a return statement
	elif operator == "exit":
		assembly = assembly + "call exit\n"

	# Generating assembly code if the tac is a print
	elif operator == "print":
		operand = instruction[2]
		if not isnumber(operand):
			loc = getlocation(operand)
			if not loc == "mem":
				assembly = assembly + "pushl " + loc + "\n"
				assembly = assembly + "pushl $str\n"
				assembly = assembly + "call printf\n"
			else:
				assembly = assembly + "pushl " + operand + "\n"
				assembly = assembly + "pushl $str\n"
				assembly = assembly + "call printf\n"
		else:
			assembly = assembly + "pushl $" + operand + "\n"
			assembly = assembly + "pushl $str\n"
			assembly = assembly + "call printf\n"			

	# Generating code for assignment operations
	elif operator == '=':
		destination = instruction[2]
		source = instruction[3]
		loc1 = getlocation(destination)
		# If the source is a literal then we can just move it to the destination
		if isnumber(source):
			if loc1 == "mem":
				assembly = assembly + "movl $" + source + ", " + destination + "\n"
			else:
				assembly = assembly + "movl $" + source + ", " + loc1 + "\n"
		else:
			# If both the source and the destination reside in the memory
			loc2 = getlocation(source)
			if loc1 == "mem" and loc2 == "mem":				
				regdest = getReg(destination, line)
				assembly = assembly + "movl " + source + ", " + regdest + "\n"
				# Update the address descriptor entry for result variable to say where it is stored no
				setregister(regdest, destination)
				setlocation(destination, regdest)			
			# If the source is in a register
			elif loc1 == "mem" and loc2 != "mem":
				regdest = getReg(destination, line)
				assembly = assembly + "movl " + loc2 + ", " + regdest + "\n"
				# Update the address descriptor entry for result variable to say where it is stored no
				setregister(regdest, destination)
				setlocation(destination, regdest)
			elif loc1 != "mem" and loc2 == "mem":
				assembly = assembly + "movl " + source + ", " + loc1 + "\n"
			elif loc1 != "mem" and loc2 != "mem":
				assembly = assembly + "movl " + loc2 + ", " + loc1 + "\n"


	# Generating the prelude for a function definition
	elif operator == "function":
		function_name = instruction[2]
		assembly = assembly + ".globl " + function_name + "\n"
		assembly = assembly + ".type "  + function_name + ", @function\n"
		assembly = assembly + function_name + ":\n"
		assembly = assembly + "pushl %ebp\n"
		assembly = assembly + "movl %esp, %ebp\n"

		
	elif operator == "arg":
		#Lno, arg, i, a_i -----> Move parameter i to var a_i
		i = instruction[2]
		a = instruction[3]
		displacement = 4*i + 4
		assembly = assembly + "movl " + str(displacement) + "(%ebp), " + a + "\n"

	elif operator == "pop":
		#LNo, pop, n
		n = instruction[2]
		assembly = assembly + "addl $4, $esp\n"

	# Generating the conclude of the function
	elif operator == "return":
		#LNo, return, val
		val = instruction[2]
		for var in varlist:
			loc = getlocation(var)
			if loc == "%eax":
				assembly = assembly + "movl " + loc + ", " + var + "\n"
				setlocation(var, "mem")
				break
		if isnumber(val):
			val = "$" + val
		assembly = assembly + "movl " + val + ", %eax\n"
		assembly = assembly + "movl %ebp, %esp\n"
		assembly = assembly + "popl %ebp\n"
		assembly = assembly + "ret\n"

	#Logical Left Shift : TAC Syntax ---> Line No, <<, result, num, count
	#corres to result = num << count

	elif operator == "~":
		#Line, not, result, op1
		result = instruction[2]
		operand1 = instruction[3]		#num
		if isnumber(operand1):
			#Case : result = !(1)
			# Get the register to store the result
			regdest = getReg(result, line)
			assembly = assembly + "movl $" + str(not(int(operand1))) + ", " + regdest + "\n"
			# Update the address descriptor entry for result variable to say where it is stored no
			setregister(regdest, result)
			setlocation(result, regdest)
		elif not isnumber(operand1):
			#case result = !(a)
			# Get the register to store the result
			regdest = getReg(result, line)
			loc1 = getlocation(operand1)
			# Move a to regdest, result = a
			if loc1 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + regdest + "\n"
			else:
				assembly = assembly + "movl " + operand1 + ", " + regdest + "\n"
			# Perform Logical and result = !(result)
			assembly = assembly + "not $" + operand2 + ", " + regdest + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)
	# Return the assembly code

	elif operator == '<=':
		result = instruction[2]
		operand1 = instruction[3]
		operand2 = instruction[4]
		LT = "LT"+str(relcount)
		NLT = "NLT"+str(relcount)
		if isnumber(operand1) and isnumber(operand2):
			#case: result = 4 < 5
			# Get the register to store the result
			regdest = getReg(result, line)
			assembly = assembly + "movl $" + str(int(int(operand1)<=int(operand2))) + ", " + regdest + "\n"
			# Update the address descriptor entry for result variable to say where it is stored no
			setregister(regdest, result)
			setlocation(result, regdest)
		elif isnumber(operand1) and not isnumber(operand2):
			#case: result = 5 < x
			# Get the register to store the result
			regdest = getReg(result, line)
			loc2 = getlocation(operand2)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand1 + ", " + regdest + "\n"
			if loc2 != "mem":
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand2 + ", " + regdest + "\n"
			assembly = assembly + "jle " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			loc1 = getlocation(operand1)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand2 + ", " + regdest + "\n"
			# Add the other operand to the register content
			if loc1 != "mem":
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"
			assembly = assembly + "jle " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and not isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			# Get the locations of the operands
			loc1 = getlocation(operand1)
			loc2 = getlocation(operand2)
			if loc1 != "mem" and loc2 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 != "mem":
				assembly = assembly + "movl " + operand1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 != "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"					
			# Update the register descriptor entry for regdest to say that it contains the result
			assembly = assembly + "jle " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			# Update the address descriptor entry for result variable to say where it is stored now
			setlocation(result, regdest)
		relcount = relcount + 1

	elif operator == '>=':
		result = instruction[2]
		operand1 = instruction[3]
		operand2 = instruction[4]
		LT = "LT"+str(relcount)
		NLT = "NLT"+str(relcount)
		if isnumber(operand1) and isnumber(operand2):
			#case: result = 4 < 5
			# Get the register to store the result
			regdest = getReg(result, line)
			assembly = assembly + "movl $" + str(int(int(operand1)>=int(operand2))) + ", " + regdest + "\n"
			# Update the address descriptor entry for result variable to say where it is stored no
			setregister(regdest, result)
			setlocation(result, regdest)
		elif isnumber(operand1) and not isnumber(operand2):
			#case: result = 5 < x
			# Get the register to store the result
			regdest = getReg(result, line)
			loc2 = getlocation(operand2)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand1 + ", " + regdest + "\n"
			if loc2 != "mem":
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand2 + ", " + regdest + "\n"
			assembly = assembly + "jge " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			loc1 = getlocation(operand1)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand2 + ", " + regdest + "\n"
			# Add the other operand to the register content
			if loc1 != "mem":
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"
			assembly = assembly + "jge " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and not isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			# Get the locations of the operands
			loc1 = getlocation(operand1)
			loc2 = getlocation(operand2)
			if loc1 != "mem" and loc2 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 != "mem":
				assembly = assembly + "movl " + operand1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 != "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"					
			# Update the register descriptor entry for regdest to say that it contains the result
			assembly = assembly + "jge " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			# Update the address descriptor entry for result variable to say where it is stored now
			setlocation(result, regdest)
		relcount = relcount + 1

	elif operator == '==':
		result = instruction[2]
		operand1 = instruction[3]
		operand2 = instruction[4]
		LT = "LT"+str(relcount)
		NLT = "NLT"+str(relcount)
		if isnumber(operand1) and isnumber(operand2):
			#case: result = 4 < 5
			# Get the register to store the result
			regdest = getReg(result, line)
			assembly = assembly + "movl $" + str(int(int(operand1)==int(operand2))) + ", " + regdest + "\n"
			# Update the address descriptor entry for result variable to say where it is stored no
			setregister(regdest, result)
			setlocation(result, regdest)
		elif isnumber(operand1) and not isnumber(operand2):
			#case: result = 5 < x
			# Get the register to store the result
			regdest = getReg(result, line)
			loc2 = getlocation(operand2)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand1 + ", " + regdest + "\n"
			if loc2 != "mem":
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand2 + ", " + regdest + "\n"
			assembly = assembly + "je " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			loc1 = getlocation(operand1)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand2 + ", " + regdest + "\n"
			# Add the other operand to the register content
			if loc1 != "mem":
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"
			assembly = assembly + "je " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and not isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			# Get the locations of the operands
			loc1 = getlocation(operand1)
			loc2 = getlocation(operand2)
			if loc1 != "mem" and loc2 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 != "mem":
				assembly = assembly + "movl " + operand1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 != "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"					
			# Update the register descriptor entry for regdest to say that it contains the result
			assembly = assembly + "je " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			# Update the address descriptor entry for result variable to say where it is stored now
			setlocation(result, regdest)
		relcount = relcount + 1

	elif operator == '!=':
		result = instruction[2]
		operand1 = instruction[3]
		operand2 = instruction[4]
		LT = "LT"+str(relcount)
		NLT = "NLT"+str(relcount)
		if isnumber(operand1) and isnumber(operand2):
			#case: result = 4 < 5
			# Get the register to store the result
			regdest = getReg(result, line)
			assembly = assembly + "movl $" + str(int(int(operand1)!=int(operand2))) + ", " + regdest + "\n"
			# Update the address descriptor entry for result variable to say where it is stored no
			setregister(regdest, result)
			setlocation(result, regdest)
		elif isnumber(operand1) and not isnumber(operand2):
			#case: result = 5 < x
			# Get the register to store the result
			regdest = getReg(result, line)
			loc2 = getlocation(operand2)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand1 + ", " + regdest + "\n"
			if loc2 != "mem":
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand2 + ", " + regdest + "\n"
			assembly = assembly + "jne " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			loc1 = getlocation(operand1)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand2 + ", " + regdest + "\n"
			# Add the other operand to the register content
			if loc1 != "mem":
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"
			assembly = assembly + "jne " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and not isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			# Get the locations of the operands
			loc1 = getlocation(operand1)
			loc2 = getlocation(operand2)
			if loc1 != "mem" and loc2 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 != "mem":
				assembly = assembly + "movl " + operand1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 != "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"					
			# Update the register descriptor entry for regdest to say that it contains the result
			assembly = assembly + "jne " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			# Update the address descriptor entry for result variable to say where it is stored now
			setlocation(result, regdest)
		relcount = relcount + 1

	elif operator == '<':
		result = instruction[2]
		operand1 = instruction[3]
		operand2 = instruction[4]
		LT = "LT"+str(relcount)
		NLT = "NLT"+str(relcount)
		if isnumber(operand1) and isnumber(operand2):
			#case: result = 4 < 5
			# Get the register to store the result
			regdest = getReg(result, line)
			assembly = assembly + "movl $" + str(int(int(operand1)<int(operand2))) + ", " + regdest + "\n"
			# Update the address descriptor entry for result variable to say where it is stored no
			setregister(regdest, result)
			setlocation(result, regdest)
		elif isnumber(operand1) and not isnumber(operand2):
			#case: result = 5 < x
			# Get the register to store the result
			regdest = getReg(result, line)
			loc2 = getlocation(operand2)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand1 + ", " + regdest + "\n"
			if loc2 != "mem":
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand2 + ", " + regdest + "\n"
			assembly = assembly + "jl " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			loc1 = getlocation(operand1)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand2 + ", " + regdest + "\n"
			# Add the other operand to the register content
			if loc1 != "mem":
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"
			assembly = assembly + "jl " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and not isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			# Get the locations of the operands
			loc1 = getlocation(operand1)
			loc2 = getlocation(operand2)
			if loc1 != "mem" and loc2 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 != "mem":
				assembly = assembly + "movl " + operand1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 != "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"					
			# Update the register descriptor entry for regdest to say that it contains the result
			assembly = assembly + "jl " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			# Update the address descriptor entry for result variable to say where it is stored now
			setlocation(result, regdest)
		relcount = relcount + 1
		
	elif operator == '>':
		result = instruction[2]
		operand1 = instruction[3]
		operand2 = instruction[4]
		LT = "LT"+str(relcount)
		NLT = "NLT"+str(relcount)
		if isnumber(operand1) and isnumber(operand2):
			#case: result = 4 < 5
			# Get the register to store the result
			regdest = getReg(result, line)
			assembly = assembly + "movl $" + str(int(int(operand1)>int(operand2))) + ", " + regdest + "\n"
			# Update the address descriptor entry for result variable to say where it is stored no
			setregister(regdest, result)
			setlocation(result, regdest)
		elif isnumber(operand1) and not isnumber(operand2):
			#case: result = 5 < x
			# Get the register to store the result
			regdest = getReg(result, line)
			loc2 = getlocation(operand2)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand1 + ", " + regdest + "\n"
			if loc2 != "mem":
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand2 + ", " + regdest + "\n"
			assembly = assembly + "jg " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			loc1 = getlocation(operand1)
			# Move the first operand to the destination register
			assembly = assembly + "movl $" + operand2 + ", " + regdest + "\n"
			# Add the other operand to the register content
			if loc1 != "mem":
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			else:
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"
			assembly = assembly + "jg " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			setlocation(result, regdest)				
		elif not isnumber(operand1) and not isnumber(operand2):
			# Get the register to store the result
			regdest = getReg(result, line)
			# Get the locations of the operands
			loc1 = getlocation(operand1)
			loc2 = getlocation(operand2)
			if loc1 != "mem" and loc2 != "mem":
				assembly = assembly + "movl " + loc1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 != "mem":
				assembly = assembly + "movl " + operand1 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc2 + ", " + regdest + "\n"
			elif loc1 != "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + loc1 + ", " + regdest + "\n"
			elif loc1 == "mem" and loc2 == "mem":
				assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "cmpl " + operand1 + ", " + regdest + "\n"					
			# Update the register descriptor entry for regdest to say that it contains the result
			assembly = assembly + "jg " + LT + "\n"
			assembly = assembly + "movl $0, " + regdest + "\n"
			assembly = assembly + "jmp NLT" + "\n"
			assembly = assembly + LT + ":" + "\n"
			assembly = assembly + "movl $1, " + regdest + "\n"
			assembly = assembly + NLT + ":" + "\n"
			setregister(regdest, result)
			# Update the address descriptor entry for result variable to say where it is stored now
			setlocation(result, regdest)
		relcount = relcount + 1

	return assembly

###################################################################################################

# Load the intermediate representation of the program from a file
irfile = open(filename, 'r')
ircode = irfile.read()
ircode = ircode.strip('\n')

# Consruct the instruction list
instrlist = []
instrlist = ircode.split('\n')

nextuseTable = [None for i in range(len(instrlist))]

# Construct the variable list and the address discriptor table
for instr in instrlist:
	templist = instr.split(', ')
	if templist[1] not in ['label', 'call', 'function']:
		varlist = varlist + templist 
varlist = list(set(varlist))
varlist = [x for x in varlist if not isnumber(x)]
for word in tackeywords:
	if word in varlist:
		varlist.remove(word)
addressDescriptor = addressDescriptor.fromkeys(varlist, "mem")
symbolTable = addressDescriptor.fromkeys(varlist, ["live", None])

# Get the leaders
leaders = [1,]
for i in range(len(instrlist)):
	instrlist[i] = instrlist[i].split(', ')
	if 'ifgoto' in instrlist[i]:
		leaders.append(int(instrlist[i][-1]))
		leaders.append(int(instrlist[i][0])+1)
	elif 'goto' in instrlist[i]:
		leaders.append(int(instrlist[i][-1]))
		leaders.append(int(instrlist[i][0])+1)
	elif 'function' in instrlist[i]:
		leaders.append(int(instrlist[i][0]))
	elif 'label' in instrlist[i]:
		leaders.append(int(instrlist[i][0]))
leaders = list(set(leaders))
leaders.sort()

# Constructing the Basic Blocks as nodes
nodes = []
i = 0
while i < len(leaders)-1:
	nodes.append(list(range(leaders[i],leaders[i+1])))
	i = i + 1
nodes.append(list(range(leaders[i],len(instrlist)+1)))

# Constructing the next use table
for node in nodes:
	revlist=node.copy()
	revlist.reverse()
	for instrnumber in revlist:
		# Get the current instruction and the operator and the operands
		instr = instrlist[instrnumber - 1]
		operator = instr[1]
		# Get the variable names in the current istruction
		variables = [x for x in instr if x in varlist]
		# Set the next use values here
		nextuseTable[instrnumber-1] = {var:symbolTable[var] for var in varlist}
		# Rule for mathematical operations
		if operator in mathops:
			z = instr[2]
			x = instr[3]
			y = instr[4]
			if z in variables:
				symbolTable[z] = ["dead", None]
			if x in variables:
				symbolTable[x] = ["live", instrnumber]
			if y in variables:
				symbolTable[y] = ["live", instrnumber]
		elif operator == "ifgoto":
			x = instr[3]
			y = instr[4]
			if x in variables:
				symbolTable[x] = ["live", instrnumber]
			if y in variables:
				symbolTable[y] = ["live", instrnumber]
		elif operator == "print":
			x = instr[2]
			if x in variables:
				symbolTable[x] = ["live", instrnumber]			
		elif operator == "=":
			x = instr[2]
			y = instr[3]
			if x in variables:
				symbolTable[x] = ["dead", None]
			if y in variables:
				symbolTable[y] = ["live", instrnumber]					

		i = i - 1

# Generating the x86 Assembly code
#--------------------------------------------------------------------------------------------------
data_section = ".section .data\n"
for var in varlist:
	data_section = data_section + var + ":\n" + ".int 0\n"
data_section = data_section + "str:\n.ascii \"%d\\n\\0\"\n"

bss_section = ".section .bss\n"
text_section = ".section .text\n" + ".globl main\n" + "main:\n"

for node in nodes:
	text_section = text_section + "L" + str(node[0]) + ":\n"
	for n in node:
		text_section = text_section + translate(instrlist[n-1])

#--------------------------------------------------------------------------------------------------

# Priniting the final output
# print("Assembly Code (x86) for: [" + filename + "]")
# print("--------------------------------------------------------------------")
x86c = data_section + bss_section + text_section
print(x86c) 
# print("--------------------------------------------------------------------")

# Save the x86 code in a file here as output.s

###################################################################################################

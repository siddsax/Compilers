		elif operator == '-':
			if isnumber(operand1) and isnumber(operand2):
				# Get the register to store the result
				regdest = getReg(result, line)
				assembly = assembly + "movl $" + str(int(operand2)-int(operand1)) + ", " + regdest + "\n"
				# Update the address descriptor entry for result variable to say where it is stored no
				setregister(regdest, result)
				setlocation(result, regdest)
			elif isnumber(operand1) and not isnumber(operand2):
				# Get the register to store the result
				regdest = getReg(result, line)
				loc2 = getlocation(operand2)
				# Move the first operand to the destination register
				if loc2 != "mem":
					assembly = assembly + "movl " + loc2 + ", " + regdest + "\n"
				else:
					assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
				assembly = assembly + "subl $" + operand1 + ", " + regdest + "\n"
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
					assembly = assembly + "subl " + loc1 + ", " + regdest + "\n"
				else:
					assembly = assembly + "subl " + operand1 + ", " + regdest + "\n"
				setregister(regdest, result)
				setlocation(result, regdest)				
			elif not isnumber(operand1) and not isnumber(operand2):
				# Get the register to store the result
				regdest = getReg(result, line)
				# Get the locations of the operands
				loc1 = getlocation(operand1)
				loc2 = getlocation(operand2)
				if loc1 != "mem" and loc2 != "mem":
					assembly = assembly + "movl " + loc2 + ", " + regdest + "\n"
					assembly = assembly + "subl " + loc1 + ", " + regdest + "\n"
				elif loc1 == "mem" and loc2 != "mem":
					assembly = assembly + "movl " + loc2 + ", " + regdest + "\n"
					assembly = assembly + "subl " + operand1 + ", " + regdest + "\n"
				elif loc1 != "mem" and loc2 == "mem":
					assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
					assembly = assembly + "subl " + loc1 + ", " + regdest + "\n"
				elif loc1 == "mem" and loc2 == "mem":
					assembly = assembly + "movl " + operand2 + ", " + regdest + "\n"
					assembly = assembly + "subl " + operand1 + ", " + regdest + "\n"					
				# Update the register descriptor entry for regdest to say that it contains the result
				setregister(regdest, result)
				# Update the address descriptor entry for result variable to say where it is stored now
				setlocation(result, regdest)				

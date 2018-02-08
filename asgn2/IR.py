import sys 

# <line number,operator, operator_specific >
# # Assignment
# # =
# operator_specific := destination,target
# # + , -, /, %, .....
# operator_specific := destination,arg1,arg2

# # conditional
# # if
# operator_specific := condition_op,arg1,arg2,line_no

# # ------------------------------------

# # function def
# line_number, label, function_name
# # function return
# line_number, return, variable_name
# line_number, return

# # Goto
# line_number, goto, line_number_to_jump

# # Print
# line_number, print, arg

# # Scan 
# line_number, scan, targ_var

# # Exit
# line_number, Exit

# # function all - assign
# line_number, fc, label, =, target
# line_number, fc, label



class IR:

	def __init__(self,filename):
		irfile = open(filename, 'r')
		ircode = irfile.read()
		ircode = ircode.strip('\n')

		# Consruct the instruction list
		self.instrlist = []
		self.instrlist = ircode.split('\n')

		self.instrtype = ['=', '+', '-', '/', '*', '%', 'conditional_goto', 'goto', 'fn_call', 'fn_def', 'print', 'scan', 'return', 'exit',]
		self.Blocks = self.Build_Blocks() #  dict { leader_no. : last_line_no }
		self.variable_list = self.Build_varlist()
		self.next_use_table,self.lineVars = self.Build_next_use_table() # list of dicts(blocks) where each key(variables) is a list pf list (use lines of that var in that live range)

	def Build_Blocks(self):
		Blocks = {}
		# get leaders
		leaders = [1]
		for instr in self.instrlist:
			instr = instr.split(', ')
			if((instr[1]=='conditional_goto') or (instr[1] == 'goto')):
				leaders.append(int(instr[0])+1)
				leaders.append(int(instr[-1]))
			if((instr[1]=='fn_call') or (instr[1]=='fn_def')):
				leaders.append(int(instr[0]))

		leaders = list(set(leaders))
		leaders.sort()
		for i in range(len(leaders)-1):
			Blocks[leaders[i]] = leaders[i+1]-1

		Blocks[leaders[-1]] = int(self.instrlist[-1].split(', ')[0])
		return Blocks


	def Build_varlist(self):
		varz = []
		for instr in self.instrlist:
			instr = instr.split(', ')
			if(instr[1] == '=' or instr[1] == 'scan' or instr[1] == '+' or instr[1] == '-' or instr[1] == '*' or instr[1] == '/' or instr[1] == '%'):
				var = instr[2]
				if(var not in varz):
					varz.append(var)
		return varz

	def Build_next_use_table(self):
		table = {} # dict of dicts of dicts
		lineVars = {}
		for start, end in self.Blocks.iteritems():	
			line = {}
			line_2 = {}
			for i in range(end, start-1, -1):
				if start == end:
					line[i] = {}

				else:
					if i is not end:
						instr = self.instrlist[i]
						instr = instr.split(', ')
						line[i] = dict(line[i+1])
						for v in varz["killed"]:
							line[i][v] = 0
						for v in varz["used"]:
							line[i][v] = int(instr[0])
					else:
						line[i] = {}
				instr = self.instrlist[i-1]
				instr = instr.split(', ')
				varz = self.parser(instr)

				line_2[i] = []
				for v in varz["killed"]:
					line_2[i].append(v)
				for v in varz["used"]:
					line_2[i].append(v)

			table[start] = line
			lineVars[start] = line_2
		return table,lineVars

	def parser(self,instr):

		varz = {
			"killed" : [],
			"used"   : []
		}

		if instr[1] == '=':
			varz["killed"].append(instr[-2])
			if instr[-1] in self.variable_list:
				varz["used"].append(instr[-1])

		if instr[1] == '+' or instr[1] == '-' or instr[1] == '*' or instr[1] == '/' or instr[1] == '%':
			varz["killed"].append(instr[-3])
			if instr[-1] in self.variable_list:
				varz["used"].append(instr[-1])
			if instr[-2] in self.variable_list:
				varz["used"].append(instr[-2])

		if instr[1] == 'conditional_goto':
			if instr[-3] in self.variable_list:
				varz["used"].append(instr[-3])
			if instr[-2] in self.variable_list:
				varz["used"].append(instr[-2])

		if instr[1] == 'print':
			if instr[-1] in self.variable_list:
				varz["used"].append(instr[-1])

		if instr[1] == 'scan':
			varz["killed"].append(instr[-1])

		if instr[1] == 'return':
			if instr[-1] in self.variable_list:
				varz["used"].append(instr[-1])			
				
		return varz
		
example = IR('example.ir')
# print(example.next_use_table)
table = example.next_use_table
varz = example.lineVars
for keys, vals in table.iteritems():
	print(keys)
	print(vals)
	print('================================')

print("---------------")
for keys, vals in varz.iteritems():
	print(keys)
	print(vals)
	print('================================')

# print(example.variable_list)
			


			# if(bb_no == 0):
			# 	bb_no = int(instr[0])
			
			# if((instr[1]=='conditional_goto') or (instr[1]=='goto')):
			# 	Blocks[bb_no] = int(instr[0])	
			# 	bb_no = 0

			# if((instr[1]=='fn_call') or (instr[1]=='fn_def')):
			# 	Blocks[bb_no-1] = int(instr[0])-1
			# 	bb_no = 0




# nextuseTable = [None for i in range(len(instrlist))]

# # Construct the variable list and the address discriptor table
# for instr in instrlist:
# 	templist = instr.split(', ')
# 	if templist[1] not in ['label', 'call', 'function']:
# 		varlist = varlist + templist 
# varlist = list(set(varlist))
# varlist = [x for x in varlist if not isnumber(x)]
# for word in tackeywords:
# 	if word in varlist:
# 		varlist.remove(word)
# addressDescriptor = addressDescriptor.fromkeys(varlist, "mem")
# symbolTable = addressDescriptor.fromkeys(varlist, ["live", None])


# # Constructing the next use table
# for node in nodes:
# 	revlist=node.copy()
# 	revlist.reverse()
# 	for instrnumber in revlist:
# 		# Get the current instruction and the operator and the operands
# 		instr = instrlist[instrnumber - 1]
# 		operator = instr[1]
# 		# Get the variable names in the current istruction
# 		variables = [x for x in instr if x in varlist]
# 		# Set the next use values here
# 		nextuseTable[instrnumber-1] = {var:symbolTable[var] for var in varlist}
# 		# Rule for mathematical operations
# 		if operator in mathops:
# 			z = instr[2]
# 			x = instr[3]
# 			y = instr[4]
# 			if z in variables:
# 				symbolTable[z] = ["dead", None]
# 			if x in variables:
# 				symbolTable[x] = ["live", instrnumber]
# 			if y in variables:
# 				symbolTable[y] = ["live", instrnumber]
# 		elif operator == "ifgoto":
# 			x = instr[3]
# 			y = instr[4]
# 			if x in variables:
# 				symbolTable[x] = ["live", instrnumber]
# 			if y in variables:
# 				symbolTable[y] = ["live", instrnumber]
# 		elif operator == "print":
# 			x = instr[2]
# 			if x in variables:
# 				symbolTable[x] = ["live", instrnumber]			
# 		elif operator == "=":
# 			x = instr[2]
# 			y = instr[3]
# 			if x in variables:
# 				symbolTable[x] = ["dead", None]
# 			if y in variables:
# 				symbolTable[y] = ["live", instrnumber]					

# 		i = i - 1

# # Generating the x86 Assembly code
# #--------------------------------------------------------------------------------------------------
# data_section = ".section .data\n"
# for var in varlist:
# 	data_section = data_section + var + ":\n" + ".int 0\n"
# data_section = data_section + "str:\n.ascii \"%d\\n\\0\"\n"

# bss_section = ".section .bss\n"
# text_section = ".section .text\n" + ".globl main\n" + "main:\n"

# for node in nodes:
# 	text_section = text_section + "L" + str(node[0]) + ":\n"
# 	for n in node:
# 		text_section = text_section + translate(instrlist[n-1])

# #--------------------------------------------------------------------------------------------------

# # Priniting the final output
# # print("Assembly Code (x86) for: [" + filename + "]")
# # print("--------------------------------------------------------------------")
# x86c = data_section + bss_section + text_section
# print(x86c) 
# # print("--------------------------------------------------------------------")

# # Save the x86 code in a file here as output.s

#!/usr/bin/env/python3
from translate import translate
from IR import IR 
from reg import Reg
import sys
import collections

file = sys.argv[1]
example = IR(file)
registers = Reg()

# Generating the x86 Assembly code
#--------------------------------------------------------------------------------------------------
data_section = ".section .data\n"
for var in list(set(example.variable_list)):
	data_section += var + ":\n" + '\t'+".int 0\n"
data_section += 'format:\n'+'\t' + '.ascii \"%d\\0\"\n'
data_section += 'format1:\n'+'\t' + '.ascii \"%d\\n\\0\"\n'
data_section += 'format2:\n'+'\t' + '.ascii \"%c\\n\\0\"\n'


for var, num in zip(example.arr_varz.keys(), example.arr_varz.values()):
	# data_section += var + ":  .fill " + str(int((num+1)/2)) + '\n'
	data_section += var + ":  .fill " + str(num) + ', 4, 0 \n'

	#data_section += var + ":\n" + '\t'+".int 0\n"

bss_section = ".section .bss\n"
text_section = ".section .text\n" + ".globl main\n" + "main:\n"

# text_section+=
# print(example.Blocks.items())
for key,val in example.Blocks.items():
	flag = 0
	fl2 = 0
	for line in range(key,val+1):
		# print(line)
		# if line is not 1:
		# 	print(line == key)	
		# 	print(example.instrlist[line-1].split(', ')[1] == 'conditional_goto')
		# 	print(example.instrlist)
		# 	if len(example.instrlist[line].split(', ')) >1:
		# 		print((example.instrlist[line].split(', ')[1] is not 'goto'))
		# 	print(line)
		# 	print(example.instrlist[line-1].split(', ')[1])
		# 	print(example.instrlist[line].split(', ')[1])
		# 	print(key)
		# 	print("----------")

		# if line is not 1 and (line == key) and (example.instrlist[line-2].split(', ')[1] == 'conditional_goto') \
		# 	and (example.instrlist[line-1].split(', ')[1] != 'goto') and (line is not 2):
		# 	print("==================oooooooo")
		# 	print(example.instrlist[line-1].split(', ')[1])
		# 	print(example.instrlist[line-2].split(', ')[1])
		# 	fl2 = 1
		# 	text_section += "## loading\n"
		# 	nextUseList = example.next_use_table[key][key]
		# 	nextUseList = collections.OrderedDict(sorted(nextUseList.items(),key=lambda x:x[1]))
		# 	indx = 0
		# 	lst = registers.regdict.keys()
		# 	lst  = list(lst)
		# 	for k, v in nextUseList.items():
		# 		registers.regdict[lst[indx]] = k
		# 		example.address_descriptor[k] = lst[indx]
		# 		if(k in example.arr_varz.keys()):
		# 			text_section += 'movl $' + k + ', '+ lst[indx] + '\n'
		# 		else:
		# 			text_section += 'movl (' + k + '), ' +  lst[indx] + '\n'
		# 		indx+=1 
		# 		if(indx==4):
		# 			break

		# elif (line == key+1 and line is not 2 and fl2 == 0):
		# 	text_section += "## loading\n"
		# 	nextUseList = example.next_use_table[key][key]
		# 	nextUseList = collections.OrderedDict(sorted(nextUseList.items(),key=lambda x:x[1]))
		# 	indx = 0
		# 	lst = registers.regdict.keys()
		# 	lst  = list(lst)
		# 	for k, v in nextUseList.items():
		# 		registers.regdict[lst[indx]] = k
		# 		example.address_descriptor[k] = lst[indx]
		# 		if(k in example.arr_varz.keys()):
		# 			text_section += 'movl $' + k + ', '+ lst[indx] + '\n'
		# 		else:
		# 			text_section += 'movl (' + k + '), ' +  lst[indx] + '\n'
		# 		indx+=1 
		# 		if(indx==4):
		# 			break

		if(example.instrlist[line-1].split(', ')[1] == 'goto' or example.instrlist[line-1].split(', ')[1] \
	        == 'conditional_goto' or example.instrlist[line-1].split(', ')[1] == 'return' or example.instrlist[line-1].split(', ')[1] == 'fn_call_1' or example.instrlist[line-1].split(', ')[1] == 'fn_call_2' or example.instrlist[line-1].split(', ')[1] == 'label'):
			text_section += "### Flushing -----------\n"
			for reg,var in registers.regdict.items():
				if var is not "":
					text_section += '\t' + "movl " + reg + ", " + var + "\n"
					registers.regdict[reg] = ""
					example.address_descriptor[var] = var
			text_section+= "### Flushed ------------\n"
			flag=1

		generated_code,example,registers = translate(example.instrlist[line-1], key, example, registers)
		text_section += generated_code

		if(flag == 0 and line == val):
			text_section += "### Flushing -----------\n"
			for reg,var in registers.regdict.items():
				if var is not "":
					if var in example.arr_varz.keys():
						registers.regdict[reg] = ""
						example.address_descriptor[var] = var
					else:
						text_section += '\t' + "movl " + reg + ", " + var + "\n"
						registers.regdict[reg] = ""
						example.address_descriptor[var] = var
			text_section+= "### Flushed ------------\n"

FinalCode = data_section + bss_section + text_section
f = open('out.s', 'w')
f.write(FinalCode)
f.close()
# print(FinalCode) 

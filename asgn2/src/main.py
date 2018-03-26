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

bss_section = ".section .bss\n"
text_section = ".section .text\n" + ".globl main\n" + "main:\n"

for key,val in example.Blocks.items():
	flag = 0
	for line in range(key,val+1):

		if (line == key+1 and line is not 2):
			text_section += "## loading\n"
			nextUseList = example.next_use_table[key][key]
			nextUseList = collections.OrderedDict(sorted(nextUseList.items(),key=lambda x:x[1]))
			indx = 0
			lst = registers.regdict.keys()
			lst  = list(lst)
			for k, v in nextUseList.items():
				registers.regdict[lst[indx]] = k
				example.address_descriptor[k] = lst[indx]
				text_section += 'movl (' + k + '), ' +  lst[indx] + '\n'
				indx+=1 
				if(indx==4):
					break

		if(example.instrlist[line-1].split(', ')[1] == 'goto' or example.instrlist[line-1].split(', ')[1] == 'conditional_goto' or example.instrlist[line-1].split(', ')[1] == 'return' or example.instrlist[line-1].split(', ')[1] == 'fn_call_1' or example.instrlist[line-1].split(', ')[1] == 'fn_call_2'):
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
					text_section += '\t' + "movl " + reg + ", " + var + "\n"
					registers.regdict[reg] = ""
					example.address_descriptor[var] = var
			text_section+= "### Flushed ------------\n"

FinalCode = data_section + bss_section + text_section
print(FinalCode) 

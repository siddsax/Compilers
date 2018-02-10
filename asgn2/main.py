from translate import translate
from IR import IR 
from reg import Reg
import sys

file = sys.argv[1]
example = IR(file)
registers = Reg()

# Generating the x86 Assembly code
#--------------------------------------------------------------------------------------------------
data_section = ".section .data\n"
for var in example.variable_list:
	data_section += var + ":\n" + ".int 0\n"
# data_section +=  "str:\n.ascii \"%d\\n\\0\"\n"

bss_section = ".section .bss\n"
text_section = ".section .text\n" + ".globl main\n" + "main:\n"
# print(example.instrlist)
for key,val in example.Blocks.items():
	text_section = text_section + "L" + str(key) + ":\n"
	# print(key,val)
	for line in range(key,val+1):
		# print()
		generated_code,example,registers = translate(example.instrlist[line-1], key, example, registers)
		text_section += generated_code
print("hello")
# for line in IR.ircode:
	# generated_code,example,register = translate(line,example,registers)
	# text_section += generated_code

FinalCode = data_section + bss_section + text_section
print(FinalCode) 
# table = example.next_use_table
# varz = example.lineVars
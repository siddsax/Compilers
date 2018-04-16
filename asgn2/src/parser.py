import sys

def parser(instr, variable_list):

	varz = {
		"killed" : [],
		"used"   : [],
		"op"     : []
	}
		
	if instr[1] == '=':
		if instr[3] != 'arr_init':
			varz["op"].append('=')
			varz["killed"].append(instr[-2])
			if instr[-1] in variable_list:
				varz["used"].append(instr[-1])

	if instr[1] == '+' or instr[1] == '-' or instr[1] == '*' or instr[1] == '/' or instr[1] == '%' \
		or instr[1] =='<<' or instr[1] == '>>':
		varz["op"].append('=')
		varz["killed"].append(instr[-3])
		if instr[-1] in variable_list:
			varz["used"].append(instr[-1])
		if instr[-2] in variable_list:
			varz["used"].append(instr[-2])

	if instr[1] == 'conditional_goto':
		varz["op"].append('conditional_goto')
		if instr[-3] in variable_list:
			varz["used"].append(instr[-3])
		if instr[-2] in variable_list:
			varz["used"].append(instr[-2])

	if instr[1] == 'print':
		varz["op"].append('print')
		if instr[-1] in variable_list:
			varz["used"].append(instr[-1])

	if instr[1] == 'scan':
		varz["op"].append('scan')
		varz["killed"].append(instr[-1])

	if instr[1] == 'return':
		varz["op"].append('return')
		if instr[-1] in variable_list:
			varz["used"].append(instr[-1])			
	if instr[1] == 'conditional_goto':
		varz["op"].append('conditional_goto')
	if instr[1] == 'goto':
		varz["op"].append('goto')
	if instr[1] == 'fn_call_1':
		varz["op"].append('fn_call')
	if instr[1] == 'fn_call_2':
		varz["killed"].append(instr[-1])
	if instr[1] == 'fn_def':
		varz["op"].append('fn_def')
	if instr[1] == 'array_asgn':
		if instr[-1] in variable_list:
			varz["used"].append(instr[-1])

	if instr[1] == 'array_access':
		varz["killed"].append(instr[2])

	return varz

#!/usr/bin/python3

import sys
import ply.yacc as yacc
from lexer import *

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	print("Use as python parser.py file.cs")
	sys.exit

# Precedence
precedence = (
	('left', 'CONOR'),
	('left', 'CONAND'),
	('left', 'OR'),
	('left', 'XOR'),
	('left', 'AND'),
	('left', 'EQ', 'NE'),
	('left', 'GT', 'GEQ', 'LT', 'LEQ'),
	('left', 'RSHIFT', 'LSHIFT'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MOD'),
	('right', 'TILDE', 'LNOT'),
	('left', 'MEMBERACCESS', 'INCREMENT', 'DECREMENT')
)

def p_start(p):
	"""start : compilation_unit
	"""

def p_compilation_unit(p):
	"""compilation_unit : class_declarations
	"""

def p_class_declarations(p):
	"""class_declarations : class_declarations class_declaration 
							| class_declaration

	"""
def p_class_declaration(p):
	"""class_declaration : class_modifiers CLASS identifier class_body TERMINATOR
							| CLASS identifier class_body TERMINATOR
							| CLASS identifier class_body
							| class_modifiers CLASS identifier class_body
	"""
def p_class_modifiers(p):
	"""class_modifiers : empty
	"""
def p_identifier(p):
	"""identifier : empty
	"""
def p_class_body(p):
	"""class_body : empty
	"""
def p_empty(p):
	"""empty : 
	"""
# def p_(p):
# 	"""
# 	"""

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

###################################################################################################
# Build the parser now
parser = yacc.yacc(start='compilation_unit', debug=True, optimize=False)

# Read the input program
inputfile = open(filename, 'r')
data = inputfile.read()
result = parser.parse(data, debug=2)

# print(result)
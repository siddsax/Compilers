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
	"""class_modifiers : class_modifier
						| class_modifiers class_modifier
	"""
def p_class_modifier(p):
	"""class_modifier : PUBLIC
						| PRIVATE
	"""

def p_class_body(p):
	"""class_body : LBRACE class_member_declarations RBRACE 
					| LBRACE RBRACE
	"""

def p_identifier(p):
	"""identifier : IDENTIFIER
	"""
	
def p_class_member_declarations(p):
	"""class_member_declarations : class_member_declaration
									| class_member_declarations class_member_declaration
	"""

def p_class_member_declaration(p):
	"""class_member_declaration : field_declaration
									| method_declaration
									| constructor_declaration
									| destructor_declaration
	"""

def p_field_declaration(p):
	"""field_declaration : field_modifiers type variable_declarators TERMINATOR
							| type variable_declarators TERMINATOR
	"""

def p_field_modifiers(p):
	"""field_modifiers : field_modifier
						| field_modifiers field_modifier
	"""

def p_field_modifier(p):
	"""field_modifier : PUBLIC 
						| PRIVATE
	"""

def p_type(p):
	"""type : reference_type
			| type_parameter
	"""
def p_reference_type(p):
	"""reference_type : class_type
						| array_type
	"""
def p_class_type(p):
	"""class_type : type_name
					| OBJECT
	"""

def p_type_name(p):
	"""type_name : proper_identifier
	"""

def p_proper_identifier(p):
	"""proper_identifier : identifier
							| prefix identifier
	"""

def p_prefix(p):
	"""prefix : identifier MEMBERACCESS 
		| prefix identifier MEMBERACCESS 
	"""

def p_array_type(p):
	"""array_type : non_array_type LBRACKET RBRACKET
	"""

def p_non_array_type(p):
	"""non_array_type : type
	"""

def p_type_parameter(p):
	"""type_parameter : identifier
						| INT
						| CHAR
	"""


# def p_(p):
# 	"""
# 	"""

# def p_(p):
# 	"""
# 	"""


def p_variable_declarators(p):
	"""variable_declarators : variable_declarator
							| variable_declarators COMMA variable_declarator
	"""
def p_variable_declarator(p):
	"""variable_declarator : identifier
							| identifier EQUALS variable_initializer
	"""

def p_variable_initializer(p):
	"""variable_initializer : expression
							| array_initializer
	"""

def p_expression(p):
	"""expression : empty
	"""

# def p_(p):
# 	"""
# 	"""

# def p_(p):
# 	"""
# 	"""


def p_array_initializer(p):
	"""array_initializer : LBRACE variable_initializer_list RBRACE
							| LBRACE RBRACE 
							| LBRACE variable_initializer_list COMMA RBRACE
	"""

def p_variable_initializer_list(p):
	"""variable_initializer_list : variable_initializer
									| variable_initializer_list COMMA variable_initializer
	"""

# def p_(p):
# 	"""
# 	"""



def p_method_declaration(p):
	"""method_declaration : method_header
							| method_body
	"""

# def p_method_header(p):
# 	"""method_header : return_type member_name LPAREN fixed_parameters RPAREN
# 						| method_modifiers  return_type member_name LPAREN fixed_parameters RPAREN
# 						| return_type member_name LPAREN RPAREN
# 						| method_modifiers return_type member_name LPAREN RPAREN
# 	"""
def p_method_header(p):
	"""method_header : method_modifiers return_type member_name LPAREN RPAREN
	"""

def p_method_modifiers(p):
	"""method_modifiers : method_modifier
						| method_modifiers method_modifier
	"""
	
def p_method_modifier(p):
	"""method_modifier : PUBLIC
						| PRIVATE
	"""			

def p_return_type(p):
	"""return_type : type
					| VOID
	"""

def p_member_name(p):
	"""member_name : identifier
	"""

def p_method_body(p):
	"""method_body : block
					| TERMINATOR
	"""

def p_fixed_parameters(p):
	"""fixed_parameters : fixed_parameter 
						| fixed_parameters COMMA fixed_parameter
	"""

def p_fixed_parameter(p):
	"""fixed_parameter : type identifier default_argument
						| type identifier
	"""

def p_default_argument(p):
	"""default_argument : EQUALS expression
	"""

def p_constructor_declaration(p):
	"""constructor_declaration : constructor_declarator constructor_body
	"""
	
def p_constructor_declarator(p):
	"""constructor_declarator : identifier LPAREN fixed_parameters RPAREN
								| identifier LPAREN  RPAREN
	"""

def p_constructor_body(p):
	"""constructor_body : block
						| TERMINATOR
	"""

def p_destructor_declaration(p): 
	"""destructor_declaration : TILDE identifier LPAREN RPAREN destructor_body
	"""

def p_destructor_body(p):
	"""destructor_body : block
						| TERMINATOR
	"""
def p_block(p):
	"""block : LBRACE RBRACE
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
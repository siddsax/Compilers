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

# CLASS #############################################################################
def p_class_declarations(p):
	"""class_declarations : class_declarations class_declaration 
							| class_declaration

	"""
def p_class_declaration(p):
	"""class_declaration : modifiers CLASS identifier class_body TERMINATOR
							| CLASS identifier class_body TERMINATOR
							| CLASS identifier class_body
							| modifiers CLASS identifier class_body
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
	"""field_declaration : modifiers type variable_declarators TERMINATOR
							| type variable_declarators TERMINATOR
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
	"""class_type : proper_identifier
					| OBJECT
	"""


def p_proper_identifier(p):
	"""proper_identifier : prefix identifier
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
						| predefined_type
	"""

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


def p_array_initializer(p):
	"""array_initializer : LBRACE variable_initializer_list RBRACE
							| LBRACE RBRACE
							| LBRACE variable_initializer_list COMMA RBRACE
	"""

def p_variable_initializer_list(p):
	"""variable_initializer_list : variable_initializer
									| variable_initializer_list COMMA variable_initializer
	"""

def p_method_declaration(p):
	"""method_declaration : method_header
							| method_body
	"""

def p_method_header(p):
	"""method_header : return_type member_name LPAREN fixed_parameters RPAREN
 						| modifiers  return_type member_name LPAREN fixed_parameters RPAREN
 						| return_type member_name LPAREN RPAREN
 						| modifiers return_type member_name LPAREN RPAREN
 	"""

def p_modifiers(p):
	"""modifiers : modifier
						| modifiers modifier
	"""

def p_modifier(p):
	"""modifier : PUBLIC
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

# STATEMENT #######################################################################
def p_block(p):
	"""block : LBRACE RBRACE
                | LBRACE statement_list RBRACE
	"""

def p_statement_list(p):
        """statement_list : statement
                            | statement_list statement
        """

def p_statement(p):
        """statement : local_variable_declaration TERMINATOR
        | embedded_statement
        """

def p_embedded_statement(p):
        """embedded_statement : block
        | TERMINATOR
        | statement_expression TERMINATOR
        | if_statement
        | iteration_statement
        | break_statement
        | continue_statement
        | return_statement
        """

def p_break_statement(p):
        """break_statement : BREAK TERMINATOR
        """

def p_continue_statement(p):
        """continue_statement : CONTINUE TERMINATOR
        """

def p_return_statement(p):
        """return_statement : RETURN TERMINATOR
        | RETURN expression TERMINATOR
        """

def p_literal(p):
        """literal : INTCONST
        | STRCONST
        | CHARCONST
        """

def p_local_variable_declaration(p):
        """local_variable_declaration : type local_variable_declarators
        """

def p_local_variable_declarators(p):
        """local_variable_declarators : local_variable_declarator
        | local_variable_declarators COMMA local_variable_declarator
        """

def p_local_variable_declarator(p):
        """local_variable_declarator : identifier
        | identifier EQUALS local_variable_initializer
        """

def p_local_variable_initializer(p): # TODO: Can be removed to reduce conflicts
        """local_variable_initializer : expression
        """

def p_statement_expression(p):
        """statement_expression : object_creation_expression
        | assignment
        | post_increment_expression
        | post_decrement_expression
        """


def p_if_statement(p):
        """if_statement : IF LPAREN expression RPAREN embedded_statement
        | IF LPAREN expression RPAREN embedded_statement ELSE embedded_statement
        """

def p_iteration_statement(p):
        """iteration_statement : WHILE LPAREN expression RPAREN embedded_statement
        """
# EXPRESSION #####################################################################################
def p_expression(p):
	"""expression : non_assignment_expression 
					| assignment
	"""

def p_assignment(p):
	"""assignment : unary_expression assignment_operator expression
					| identifier assignment_operator expression
	"""

def p_assignment_operator(p):
	"""assignment_operator : EQUALS
							| PLUSEQUAL
							| MINUSEQUAL
	"""
def p_unary_expression(p):
	"""unary_expression : primary_expression
						| PLUS unary_expression
						| PLUS identifier
						| MINUS unary_expression
						| MINUS identifier
						| LNOT unary_expression
						| LNOT identifier
						| TILDE unary_expression
						| TILDE identifier
	"""

def p_primary_expression(p):
	"""primary_expression : primary_no_array_creation_expression
							| array_creation_expression
	"""

def p_primary_no_array_creation_expression(p):
	"""primary_no_array_creation_expression : literal
											| parenthesized_expression
											| member_access
											| element_access
											| post_increment_expression
											| post_decrement_expression
											| object_creation_expression
											| typeof_expression
	"""

def p_parenthesized_expression(p):
	"""parenthesized_expression : LPAREN expression RPAREN
	"""

def p_member_access(p):
	"""member_access : primary_expression MEMBERACCESS identifier
						| iMEMAi
						| predefined_type MEMBERACCESS identifier
	"""

def p_predefined_type(p):
	"""predefined_type : INT 
						| CHAR
	"""

def p_element_access(p):
	"""element_access : primary_no_array_creation_expression LBRACKET expression_list RBRACKET 
						| identifier LBRACKET expression_list RBRACKET
	"""

def p_expression_list(p):
	"""expression_list : expression
						| expression_list COMMA expression
	"""

def p_post_increment_expression(p):
	"""post_increment_expression : primary_expression INCREMENT
									| identifier INCREMENT
	"""

def p_post_decrement_expression(p):
	"""post_decrement_expression : primary_expression DECREMENT
									| identifier DECREMENT
	"""

def p_object_creation_expression(p):
	"""object_creation_expression : NEW type LPAREN argument_list RPAREN object_or_collection_initializer
									| NEW type LPAREN argument_list RPAREN
									| NEW type LPAREN RPAREN
									| NEW type object_or_collection_initializer
	"""

def p_argument_list(p):
	""" argument_list : argument
						| argument_list COMMA argument
	"""

def p_argument(p):
	"""argument : argument_name argument_value
				| argument_value
	"""

def p_argument_name(p):
	"""argument_name : identifier TERMINATOR
	"""

def p_argument_value(p):
	""" argument_value : expression
	"""

def p_object_or_collection_initializer(p):
	"""object_or_collection_initializer : object_initializer
										| collection_initializer
	"""

def p_object_initializer(p):
 	"""object_initializer : LBRACE member_initializer_list RBRACE
							| LBRACE RBRACE
 							| LBRACE member_initializer_list COMMA RBRACE
 	"""

def p_member_initializer_list(p):
	"""member_initializer_list : member_initializer
								| member_initializer_list COMMA member_initializer
	"""

def p_member_initializer(p):
	"""member_initializer : identifier EQUALS initializer_value
	"""

def p_initializer_value(p):
	"""initializer_value : expression
						| object_or_collection_initializer
	"""

def p_collection_initializer(p):
	"""collection_initializer : LBRACE element_initializer_list RBRACE
								| LBRACE element_initializer_list COMMA RBRACE
	"""

def p_element_initializer_list(p):
	"""element_initializer_list : element_initializer
								| element_initializer_list COMMA element_initializer
	"""

def p_element_initializer(p):
	"""element_initializer : non_assignment_expression 
							| LBRACE expression_list RBRACE
	"""

def p_array_creation_expression(p):
	"""array_creation_expression : NEW non_array_type LBRACKET expression RBRACKET
									| NEW array_type array_initializer
	"""

def p_typeof_expression(p):
	"""typeof_expression : TYPEOF LPAREN type RPAREN
				 			| TYPEOF LPAREN unbound_type_name RPAREN
	 						| TYPEOF LPAREN VOID RPAREN
	"""

def p_unbound_type_name(p):
	"""unbound_type_name : iMEMAi
							| unbound_type_name MEMBERACCESS identifier
	"""

def p_iMEMAi(p):
	"""iMEMAi : identifier MEMBERACCESS identifier
	"""
def p_non_assignment_expression(p):
	"""non_assignment_expression : conditional_expression
	"""
def p_conditional_expression(p):
	"""conditional_expression : conditional_or_expression
	"""

def p_conditional_or_expression(p):
	"""conditional_or_expression : conditional_and_expression
									| conditional_or_expression CONOR conditional_and_expression
	"""

def p_conditional_and_expression(p):
	"""conditional_and_expression : inclusive_or_expression
									| conditional_and_expression CONAND inclusive_or_expression
	"""

def p_inclusive_or_expression(p):
	"""inclusive_or_expression : exclusive_or_expression
								| inclusive_or_expression OR exclusive_or_expression
	"""

def p_exclusive_or_expression(p):
	"""exclusive_or_expression : and_expression
								| exclusive_or_expression XOR and_expression
	"""

def p_and_expression(p):
	"""and_expression : equality_expression
						| and_expression AND equality_expression
	"""

def p_equality_expression(p):
	"""equality_expression : relational_expression
							| equality_expression EQ relational_expression
							| equality_expression NE relational_expression
	"""

def p_relational_expression(p):
	""" relational_expression : shift_expression
								| relational_expression LT shift_expression
								| relational_expression GT shift_expression
								| relational_expression LEQ shift_expression
								| relational_expression GEQ shift_expression
	"""

def p_shift_expression(p):
	"""shift_expression : additive_expression
						| shift_expression LSHIFT additive_expression
						| shift_expression RSHIFT additive_expression
	"""

def p_additive_expression(p):
	"""additive_expression : multiplicative_expression
							| additive_expression PLUS multiplicative_expression 
							| additive_expression MINUS multiplicative_expression
	"""

def p_multiplicative_expression(p):
	"""multiplicative_expression : unary_expression
									| identifier
									| multiplicative_expression TIMES unary_expression
									| multiplicative_expression DIVIDE unary_expression
									| multiplicative_expression MOD unary_expression
									| multiplicative_expression TIMES identifier
									| multiplicative_expression DIVIDE identifier
									| multiplicative_expression MOD identifier
	"""

# def p_(p):
# 	"""
# 	"""

# def p_(p):
# 	"""
# 	"""
# EMPTY ##########################################################################################
# def p_empty(p):
# 	"""empty : 
# 	"""

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

##################################################################################################
# Build the parser now
parser = yacc.yacc(start='start', debug=True, optimize=False)

# Read the input program
inputfile = open(filename, 'r')
data = inputfile.read()
result = parser.parse(data, debug=2)

# print(result)

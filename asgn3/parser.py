#!/usr/bin/env python3

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
    p[0] = ['start', p[1]]

def p_compilation_unit(p):
    """compilation_unit : class_declarations
    | using_directives class_declarations
    """
    if len(p) == 2:
        p[0] = ['compilation_unit', p[1]]
    else:
        p[0] = ['compilation_unit', p[1], p[2]]

# USING #############################################################################
def p_using_directives(p):
    """using_directives : using_directive
    | using_directives using_directive
    """
    if len(p) == 2:
        p[0] = ['using_directives', p[1]]
    else:
        p[0] = ['using_directives', p[1], p[2]]

def p_using_directive(p):
    """using_directive : USING identifier TERMINATOR
    """
    p[0] = ['using_directive', 'USING', p[2], ';']
# CLASS #############################################################################
def p_class_declarations(p):
    """class_declarations : class_declarations class_declaration 
    | class_declaration
    """
    if len(p) == 3:
        p[0] = ['class_declarations', p[1], p[2]]
    else:
        p[0] = ['class_declarations', p[1]]

def p_class_declaration(p):
    """class_declaration : modifiers CLASS identifier class_body TERMINATOR
    | CLASS identifier class_body TERMINATOR
    | CLASS identifier class_body
    | modifiers CLASS identifier class_body
    """
    if len(p) == 6:
        p[0] = ['class_declaration', p[1], 'CLASS', p[3], p[4], ';']
    elif len(p) == 4:
        p[0] = ['class_declaration', 'CLASS', p[2], p[3], ';']
    elif p[1] == 'CLASS':
        p[0] = ['class_declaration', 'CLASS', p[2], p[3], ';']
    else:
        p[0] = ['class_declaration', p[1], 'CLASS', p[3], p[4], ';'];

def p_class_body(p):
    """class_body : LBRACE class_member_declarations RBRACE 
    | LBRACE RBRACE
    """
    if len(p) == 3:
        p[0] = ['class_body', '{', '}']
    else:
        p[0] = ['class_body', '{', p[2], '}']

def p_identifier(p):
    """identifier : IDENTIFIER
    """
    p[0] = ['identifier', p[1]]
    
def p_class_member_declarations(p):
    """class_member_declarations : class_member_declaration
    | class_member_declarations class_member_declaration
    """
    if len(p) == 2:
        p[0] = ['class_member_declerations', p[1]]
    else:
        p[0] = ['class_member_declerations', p[1], p[2]]

def p_class_member_declaration(p):
    """class_member_declaration : field_declaration
    | method_declaration
    | constructor_declaration
    | destructor_declaration
    """
    p[0] = ['class_member_declaration', p[1]]

def p_field_declaration(p):
    """field_declaration : modifiers type variable_declarators TERMINATOR
    | type variable_declarators TERMINATOR
    """
    if len(p) == 4:
        p[0] = ['field_declaration', p[1], p[2], ';']
    else:
        p[0] = ['field_declaration', p[1], p[2], p[3], ';']

def p_type(p):
    """type : reference_type
    | type_parameter
    """
    p[0] = ['type', p[1]]

def p_reference_type(p):
    """reference_type : class_type
    | array_type
    """
    p[0] = ['reference_type', p[1]]

def p_class_type(p):
    """class_type : proper_identifier
    | OBJECT
    """
    p[0] = ['class_type', p[1]]

def p_proper_identifier(p):
    """proper_identifier : prefix identifier
    """
    p[0] = ['proper_identifier', p[1]]

def p_prefix(p):
    """prefix : identifier MEMBERACCESS 
            | prefix identifier MEMBERACCESS 
    """
    if len(p) == 3:
        p[0] = ['prefix', p[1], '.']
    else:
        p[0] = ['prefix', p[1], p[2], '.']

def p_array_type(p):
    """array_type : non_array_type LBRACKET RBRACKET
    """
    p[0] = ['array_type', p[1], '(', ')']

def p_non_array_type(p):
    """non_array_type : type
    """
    p[0] = ['non_array_type', p[1]]

def p_type_parameter(p):
    """type_parameter : identifier
    | predefined_type
    """
    p[0] = ['type_parameter', p[1]]

def p_variable_declarators(p):
    """variable_declarators : variable_declarator
    | variable_declarators COMMA variable_declarator
    """
    if len(p) == 2:
        p[0] = ['variable_declarators', p[1]]
    else:
        p[0] = ['variable_declarators', p[1], ',', p[3]]

def p_variable_declarator(p):
    """variable_declarator : identifier
    | identifier EQUALS variable_initializer
    """
    if len(p) == 2:
        p[0] = ['variable_declarator', p[1]]
    else:
        p[0] = ['variable_declarator', p[1], '=', p[3]]

def p_variable_initializer(p):
    """variable_initializer : expression
                                                    | array_initializer
    """
    p[0] = ['variable_initializer', p[1]]

def p_array_initializer(p):
    """array_initializer : LBRACE variable_initializer_list RBRACE
                                                    | LBRACE RBRACE
                                                    | LBRACE variable_initializer_list COMMA RBRACE
    """
    if len(p) == 3:
        p[0] = ['array_initializer', '{', '}']
    elif len(p) == 4:
        p[0] = ['array_initializer', '{', p[1], '}']
    else:
        p[0] = ['array_initializer', '{', p[1], ',', '}']

def p_variable_initializer_list(p):
    """variable_initializer_list : variable_initializer
                                                                    | variable_initializer_list COMMA variable_initializer
    """
    if len(p) == 2:
        p[0] = ['variable_initializer_list', p[1]]
    else:
        p[0] = ['variable_initializer_list', p[1], ',', p[3]]

def p_method_declaration(p):
    """method_declaration : method_header
                                                    | method_body
    """
    p[0] = ['method_declaration', p[1]]

#def p_qualified_identifier(p):
#    """qualified_identifier : identifier 
#    | qualified_identifier MEMBERACCESS identifier
#    """
#    if len(p) == 2:
#        p[0] = ['qualified_identifier', p[1]]
#    else:
#        p[0] = ['qualified_identifier', p[1], p[2], p[3]]

def p_method_header(p):
    """method_header : return_type member_name LPAREN fixed_parameters RPAREN
                                            | modifiers  return_type member_name LPAREN fixed_parameters RPAREN
                                            | return_type member_name LPAREN RPAREN
                                            | modifiers return_type member_name LPAREN RPAREN
    """
    if len(p) == 7:
        p[0] = ['method_header', p[1], p[2], p[3], '(', p[5], ')']
    elif len(p) == 5:
        p[0] = ['method_header', p[1], p[2], '(', ')']
    elif p[3] == '(':
        p[0] = ['method_header', p[1], p[2], '(', p[4], ')']
    else:
        p[0] = ['method_header', p[1], p[2], p[3], '(', ')']

def p_modifiers(p):
    """modifiers : modifier
                                            | modifiers modifier
    """
    if len(p) == 2:
        p[0] = ['modifiers', p[1]]
    else:
        p[0] = ['modifiers', p[1], p[2]]

def p_modifier(p):
    """modifier : PUBLIC
                                    | PRIVATE
    """
    p[0] = ['modifier', p[1]]

def p_return_type(p):
    """return_type : type
                                    | VOID
    """
    p[0] = ['return_type', p[1]]

def p_member_name(p):
    """member_name : identifier
    """
    p[0] = ['member_name', p[1]]

def p_method_body(p):
    """method_body : block
                                    | TERMINATOR
    """
    p[0] = ['method_body', p[1]]

def p_fixed_parameters(p):
    """fixed_parameters : fixed_parameter 
                                            | fixed_parameters COMMA fixed_parameter
    """
    if len(p) == 2:
        p[0] = ['fixed_parameters', p[1]]
    else:
        p[0] = ['fixed_parameters', p[1], ',', p[3]]

def p_fixed_parameter(p):
    """fixed_parameter : type identifier default_argument
                                            | type identifier
    """
    if len(p) == 3:
        p[0] = ['fixed_parameter', p[1], p[2]]
    else:
        p[0] = ['fixed_parameter', p[1], p[2], p[3]]

def p_default_argument(p):
    """default_argument : EQUALS expression
    """
    p[0] = ['default_argument', '=', p[2]]

def p_constructor_declaration(p):
    """constructor_declaration : constructor_declarator constructor_body
    """
    p[0] = ['constructor_declaration', p[1], p[2]]
    
def p_constructor_declarator(p):
    """constructor_declarator : identifier LPAREN fixed_parameters RPAREN
                                                            | identifier LPAREN  RPAREN
    """
    if len(p) == 4:
        p[0] = ['constructor_declarator', p[1], '(', ')']
    else:
        p[0] = ['constructor_declarator', p[1], '(', p[3], ')']

def p_constructor_body(p):
    """constructor_body : block
                                            | TERMINATOR
    """
    if p[1] is ';':
        p[0] = ['constructor_body', ';']
    else:
        p[0] = ['constructor_body', p[1]]

def p_destructor_declaration(p): 
    """destructor_declaration : TILDE identifier LPAREN RPAREN destructor_body
    """
    p[0] = ['destructor_declaration', p[1], p[2], p[3], p[4], p[5]]

def p_destructor_body(p):
    """destructor_body : block
                                            | TERMINATOR
    """
    p[0] = ['destructor_body', p[1]]

# STATEMENT #######################################################################
def p_block(p):
    """block : LBRACE RBRACE
            | LBRACE statement_list RBRACE
    """
    if len(p) == 3:
        p[0] = ['block', p[1], p[2]]
    else:
        p[0] = ['block', p[1], p[2], p[3]]

def p_statement_list(p):
    """statement_list : statement
                        | statement_list statement
    """
    if len(p) == 2:
        p[0] = ['statement_list', p[1]]
    else:
        p[0] = ['statement_list', p[1], p[2]]

def p_statement(p):
    """statement : local_variable_declaration TERMINATOR
    | embedded_statement
    """
    if len(p) == 2:
        p[0] = ['statement', p[1]]
    else:
        p[0] = ['statement', p[1], p[2]]

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
    if len(p) == 2:
        p[0] = ['embedded_statement', p[1]]
    else:
        p[0] = ['embedded_statement', p[1], p[2]]

def p_break_statement(p):
    """break_statement : BREAK TERMINATOR
    """
    p[0] = ['break_statement', 'BREAK', p[2]]

def p_continue_statement(p):
    """continue_statement : CONTINUE TERMINATOR
    """
    p[0] = ['continue_statement', 'CONTINUE', p[2]]

def p_return_statement(p):
    """return_statement : RETURN TERMINATOR
    | RETURN expression TERMINATOR
    """
    if len(p) == 3:
        p[0] = ['return_statement', 'RETURN', p[2]]
    else:
        p[0] = ['return_statement', 'RETURN', p[2], p[3]]

def p_literal(p):
    """literal : INTCONST
    | STRCONST
    | CHARCONST
    """
    p[0] = ['literal', p[1]]

def p_local_variable_declaration(p):
    """local_variable_declaration : type local_variable_declarators
    """
    p[0] = ['local_variable_declaration', p[1], p[2]]

def p_local_variable_declarators(p):
    """local_variable_declarators : local_variable_declarator
    | local_variable_declarators COMMA local_variable_declarator
    """
    if len(p) == 2:
        p[0] = ['local_variable_declarators', p[1]]
    else:
        p[0] = ['local_variable_declarators', p[1], p[2], p[3]]

def p_local_variable_declarator(p):
    """local_variable_declarator : identifier
    | identifier EQUALS local_variable_initializer
    """
    if len(p) == 2:
        p[0] = ['local_variable_declarator', p[1]]
    else:
        p[0] = ['local_variable_declarator', p[1], p[2], p[3]]

def p_local_variable_initializer(p): # TODO: Can be removed to reduce conflicts
    """local_variable_initializer : expression
    """
    p[0] = ['local_variable_initializer', p[1]]

def p_statement_expression(p):
    """statement_expression : object_creation_expression
    | assignment
    | invocation_expression
    | post_increment_expression
    | post_decrement_expression
    """
    p[0] = ['statement_expression' , p[1]]

def p_invocation_expression(p):
    """invocation_expression : primary_expression LPAREN argument_list RPAREN
    | primary_expression LPAREN RPAREN
    | identifier LPAREN RPAREN
    | identifier LPAREN argument_list RPAREN
    | proper_identifier LPAREN argument_list RPAREN
    | proper_identifier LPAREN RPAREN
    """
    if len(p) == 4:
        p[0] = ['invocation_expression', p[1], p[2], p[3]]
    else:
        p[0] = ['invocation_expression', p[1], p[2], p[3], p[4]]

def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN embedded_statement
    | IF LPAREN expression RPAREN embedded_statement ELSE embedded_statement
    """
    if len(p) == 6:
        p[0] = ['if_statement', p[1], p[2], p[3], p[4], p[5]]
    else:
        p[0] = ['if_statement', p[1], p[2], p[3], p[4], p[5], p[6], p[7]]

def p_iteration_statement(p):
    """iteration_statement : WHILE LPAREN expression RPAREN embedded_statement
    """
    p[0] = ['iteration_statement', p[1], p[2], p[3], p[4], p[5]]
# EXPRESSION #####################################################################################
def p_expression(p):
    """expression : non_assignment_expression 
                                    | assignment
    """
    p[0] = ['expression', p[1]]

def p_assignment(p):
    """assignment : unary_expression assignment_operator expression
                                    | identifier assignment_operator expression
    """
    p[0] = ['assignment', p[1], p[2], p[3]]

def p_assignment_operator(p):
    """assignment_operator : EQUALS
                                                    | PLUSEQUAL
                                                    | MINUSEQUAL
    """
    p[0] = ['assignment_operator', p[1]]

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
    if len(p) == 2:
        p[0] = ['unary_expression', p[1]]
    elif len(p) == 3:
        p[0] = ['unary_expression', p[1], p[2]]
    else:
        p[0] = ['unary_expression', p[1], p[2], p[3]]

def p_primary_expression(p):
    """primary_expression : primary_no_array_creation_expression
                                                    | array_creation_expression
    """
    p[0] = ['primary_expression', p[1]]

def p_primary_no_array_creation_expression(p):
    """primary_no_array_creation_expression : literal
                                                                                    | parenthesized_expression
                                                                                    | member_access
                                                                                    | element_access
                                                                                    | post_increment_expression
                                                                                    | invocation_expression
                                                                                    | post_decrement_expression
                                                                                    | object_creation_expression
                                                                                    | typeof_expression
    """
    p[0] = ['primary_no_array_creation_expression', p[1]]

def p_parenthesized_expression(p):
    """parenthesized_expression : LPAREN expression RPAREN
    """
    p[0] = ['parenthesized_expression', p[1], p[2], p[3]]

def p_member_access(p):
    """member_access : primary_expression MEMBERACCESS identifier
                                            | iMEMAi
                                            | predefined_type MEMBERACCESS identifier
    """
    if len(p) == 2:
        p[0] = ['member_access', p[1]]
    else:
        p[0] = ['member_access', p[1], p[2], p[3]]

def p_predefined_type(p):
    """predefined_type : INT 
                                            | CHAR
    """
    p[0] = ['predefined_type', p[1]]

def p_element_access(p):
    """element_access : primary_no_array_creation_expression LBRACKET expression_list RBRACKET 
                                            | identifier LBRACKET expression_list RBRACKET
    """
    p[0] = ['element_access', p[1], p[2], p[3], p[4]]

def p_expression_list(p):
    """expression_list : expression
                                            | expression_list COMMA expression
    """
    if len(p) == 2:
        p[0] = ['expression_list', p[1]]
    else:
        p[0] = ['expression_list', p[1], p[2], p[3]]

def p_post_increment_expression(p):
    """post_increment_expression : primary_expression INCREMENT
                                                                    | identifier INCREMENT
    """
    p[0] = ['post_increment_expression', p[1], p[2]]

def p_post_decrement_expression(p):
    """post_decrement_expression : primary_expression DECREMENT
                                                                    | identifier DECREMENT
    """
    p[0] = ['post_decrement_expression', p[1], p[2]]

def p_object_creation_expression(p):
    """object_creation_expression : NEW type LPAREN argument_list RPAREN object_or_collection_initializer
                                                                    | NEW type LPAREN argument_list RPAREN
                                                                    | NEW type LPAREN RPAREN
                                                                    | NEW type object_or_collection_initializer
    """
    if len(p) == 4:
        p[0] = ['object_creation_expression', p[1], p[2], p[3]]
    elif len(p) == 5:
        p[0] = ['object_creation_expression', p[1], p[2], p[3], p[4]]
    elif len(p) == 6:
        p[0] = ['object_creation_expression', p[1], p[2], p[3], p[4], p[5]]
    else:
        p[0] = ['object_creation_expression', p[1], p[2], p[3], p[4], p[5], p[6]]

def p_argument_list(p):
    """ argument_list : argument
                                            | argument_list COMMA argument
    """
    if len(p) == 2:
        p[0] = ['argument_list', p[1]]
    else:
        p[0] = ['argument_list', p[1], p[2], p[3]]

def p_argument(p):
    """argument : argument_name argument_value
                            | argument_value
    """
    if len(p) == 2:
        p[0] = ['argument', p[1]]
    else:
        p[0] = ['argument', p[1], p[2]]

def p_argument_name(p):
    """argument_name : identifier COLON
    """
    p[0] = ['argument_name', p[1], p[2]]

def p_argument_value(p):
    """ argument_value : expression
    """
    p[0] = ['argument_value', p[1]]

def p_object_or_collection_initializer(p):
    """object_or_collection_initializer : object_initializer
                                                                            | collection_initializer
    """
    p[0] = ['object_or_collection_initializer', p[1]]

def p_object_initializer(p):
    """object_initializer : LBRACE member_initializer_list RBRACE
                                                    | LBRACE RBRACE
                                                    | LBRACE member_initializer_list COMMA RBRACE
    """
    if len(p) == 3:
        p[0] = ['object_initializer', p[1], p[2]]
    elif len(p) == 4:
        p[0] = ['object_initializer', p[1], p[2], p[3]]
    else:
        p[0] = ['object_initializer', p[1], p[2], p[3], p[4]]

def p_member_initializer_list(p):
    """member_initializer_list : member_initializer
                                                            | member_initializer_list COMMA member_initializer
    """
    if len(p) == 2:
        p[0] = ['member_initializer_list', p[1]]
    else:
        p[0] = ['member_initializer_list', p[1], p[2], p[3]]

def p_member_initializer(p):
    """member_initializer : identifier EQUALS initializer_value
    """
    p[0] = ['member_initializer', p[1], p[2], p[3]]

def p_initializer_value(p):
    """initializer_value : expression
                                            | object_or_collection_initializer
    """
    p[0] = ['initializer_value', p[1]]

def p_collection_initializer(p):
    """collection_initializer : LBRACE element_initializer_list RBRACE
                                                            | LBRACE element_initializer_list COMMA RBRACE
    """
    if len(p) == 4:
        p[0] = ['collection_initializer', p[1], p[2], p[3]]
    else:
        p[0] = ['collection_initializer', p[1], p[2], p[3], p[4]]

def p_element_initializer_list(p):
    """element_initializer_list : element_initializer
                                                            | element_initializer_list COMMA element_initializer
    """
    if len(p) == 2:
        p[0] = ['element_initializer_list', p[1]]
    else:
        p[0] = ['element_initializer_list', p[1], p[2], p[3]]

def p_element_initializer(p):
    """element_initializer : non_assignment_expression 
                                                    | LBRACE expression_list RBRACE
    """
    if len(p) == 2:
        p[0] = ['element_initializer', p[1]]
    else:
        p[0] = ['element_initializer_list', p[1], p[2], p[3]]

def p_array_creation_expression(p):
    """array_creation_expression : NEW non_array_type LBRACKET expression RBRACKET
                                                                    | NEW array_type array_initializer
    """
    if len(p) == 4:
        p[0] = ['array_creation_expression', p[1], p[2], p[3]]
    else:
        p[0] = ['array_creation_expression', p[1], p[2], p[3], p[4], p[5]]

def p_typeof_expression(p):
    """typeof_expression : TYPEOF LPAREN type RPAREN
                                                    | TYPEOF LPAREN unbound_type_name RPAREN
                                                    | TYPEOF LPAREN VOID RPAREN
    """
    p[0] = ['typeof_expression', p[1], p[2], p[3], p[4]]

def p_unbound_type_name(p):
    """unbound_type_name : iMEMAi
                                                    | unbound_type_name MEMBERACCESS identifier
    """
    if len(p) == 2:
        p[0] = ['unbound_type_name', p[1]]
    else:
        p[0] = ['unbound_type_name', p[1], p[2], p[3]]

def p_iMEMAi(p):
    """iMEMAi : identifier MEMBERACCESS identifier
    """
    p[0] = ['iMEMAi', p[1], p[2], p[3]]

def p_non_assignment_expression(p):
    """non_assignment_expression : conditional_expression
    """
    p[0] = ['non_assignment_expression', p[1]]

def p_conditional_expression(p):
    """conditional_expression : conditional_or_expression
    """
    p[0] = ['conditional_expression', p[1]]

def p_conditional_or_expression(p):
    """conditional_or_expression : conditional_and_expression
                                                                    | conditional_or_expression CONOR conditional_and_expression
    """
    if len(p) == 2:
        p[0] = ['conditional_or_expression', p[1]]
    else:
        p[0] = ['conditional_or_expression', p[1], p[2], p[3]]

def p_conditional_and_expression(p):
    """conditional_and_expression : inclusive_or_expression
                                                                    | conditional_and_expression CONAND inclusive_or_expression
    """
    if len(p) == 2:
        p[0] = ['conditional_and_expression', p[1]]
    else:
        p[0] = ['conditional_and_expression', p[1], p[2], p[3]]

def p_inclusive_or_expression(p):
    """inclusive_or_expression : exclusive_or_expression
                                                            | inclusive_or_expression OR exclusive_or_expression
    """
    if len(p) == 2:
        p[0] = ['inclusive_or_expression', p[1]]
    else:
        p[0] = ['inclusive_or_expression', p[1], p[2], p[3]]

def p_exclusive_or_expression(p):
    """exclusive_or_expression : and_expression
                                                            | exclusive_or_expression XOR and_expression
    """
    if len(p) == 2:
        p[0] = ['exclusive_or_expression', p[1]]
    else:
        p[0] = ['exclusive_or_expression', p[1], p[2], p[3]]

def p_and_expression(p):
    """and_expression : equality_expression
                                            | and_expression AND equality_expression
    """
    if len(p) == 2:
        p[0] = ['and_expression', p[1]]
    else:
        p[0] = ['and_expression', p[1], p[2], p[3]]

def p_equality_expression(p):
    """equality_expression : relational_expression
                                                    | equality_expression EQ relational_expression
                                                    | equality_expression NE relational_expression
    """
    if len(p) == 2:
        p[0] = ['equality_expression', p[1]]
    else:
        p[0] = ['equality_expression', p[1], p[2], p[3]]

def p_relational_expression(p):
    """ relational_expression : shift_expression
                                                            | relational_expression LT shift_expression
                                                            | relational_expression GT shift_expression
                                                            | relational_expression LEQ shift_expression
                                                            | relational_expression GEQ shift_expression
    """
    if len(p) == 2:
        p[0] = ['relational_expression', p[1]]
    else:
        p[0] = ['relational_expression', p[1], p[2], p[3]]

def p_shift_expression(p):
    """shift_expression : additive_expression
                                            | shift_expression LSHIFT additive_expression
                                            | shift_expression RSHIFT additive_expression
    """
    if len(p) == 2:
        p[0] = ['shift_expression', p[1]]
    else:
        p[0] = ['shift_expression', p[1], p[2], p[3]]

def p_additive_expression(p):
    """additive_expression : multiplicative_expression
                                                    | additive_expression PLUS multiplicative_expression 
                                                    | additive_expression MINUS multiplicative_expression
    """
    if len(p) == 2:
        p[0] = ['additive_expression', p[1]]
    else:
        p[0] = ['additive_expression', p[1], p[2], p[3]]

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
    if len(p) == 2:
        p[0] = ['multiplicative_expression', p[1]]
    else:
        p[0] = ['multiplicative_expression', p[1], p[2], p[3]]

# def p_(p):
#     """
#     """

# def p_(p):
#     """
#     """
# EMPTY ##########################################################################################
# def p_empty(p):
#     """empty : 
#     """

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
#print(result)

output = ""
def printf(p, prev, nxt):

    parse = ""
    if type(p) is list:
        for i in p[1:]:
            if type(i) is list:
                parse += " " + i[0]
            else:
                if i is None:
                   print('fuck')
                parse += " " + str(i)

        print(prev + " <b style='color:blue'>" + parse + "</b> " + nxt + "<br>")
        global output
        output += prev + " <b style='color:blue'>" + parse + "</b> " + nxt + "<br>\n"

        for i in range(len(p)-1, 0, -1):
            newp = prev

            for j in range(1, i):
                if type(p[j]) is list:
                    newp += " " + p[j][0]
                else:
                   newp += " " + str(p[j])

            nnxt = printf(p[i], newp, nxt)
            nxt = nnxt

        return nxt
    else:
        return str(p) + " " + nxt

print("<html>\n<head></head>\n<body>\n")
print("<b style='color:blue'>start</b><br>")
result = printf(result, "", "")
print("</body>\n</html>")

output = "<html>\n<head></head>\n<body>\n" + "<b style='color:blue'>start</b><br>\n" + output + "</body>\n</html>"
op = open('output.html', 'w+')
op.write(output)
op.close()

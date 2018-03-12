#!/usr/bin/python3

import sys
import ply.yacc as yacc
from lexer import *

#TODO: input read

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
	('left', 'MEMBERACCESS, INCREMENT, DECREMENT')
)

#!/usr/bin/python3
import ply.lex as lex
import sys

reserved = {
    'char' : 'CHAR',
    'continue' : 'CONTINUE',
    'void' : 'VOID',
    'new' : 'NEW',
    'short' : 'SHORT',
    'string' : 'STRING',
    'class' : 'CLASS',
    'private' : 'PRIVATE',
    'public' : 'PUBLIC',
    'if' : 'IF',
    'else' : 'ELSE',
    'null' : 'NULL',
    'return' : 'RETURN',
    'object' : 'OBJECT',
    'sizeof' : 'SIZEOF',
    'int' : 'INT',
    'while' : 'WHILE',
    'using'  :  'USING',
    'break' : 'BREAK',
    'goto'  : 'GOTO'
}

tokens = [
    # Literals: Identifiers, Int-Constants, Char-Constant, String-Constant 
    'IDENTIFIER', 'INTCONST', 'CHARCONST', 'STRCONST', 
    # Primary Operators: . ?. ++ -- 
    'MEMBERACCESS', 'INCREMENT', 'DECREMENT',
    # Unary Operators: ~ ! 
    'LNOT', 'TILDE',
    # Multiplicative Operators: * / %
    'TIMES', 'DIVIDE', 'MOD',
    # Additive Operators + -
    'PLUS', 'MINUS',
    # Shift Operators: << >>
    'LSHIFT', 'RSHIFT',
    # Assignment and Lambda Operators: = += -= 
    'EQUALS', 'PLUSEQUAL', 'MINUSEQUAL',
    # Others: \n // ... \'" | '\"' | '\\' | '\0' '\t' 
    'NEWLINE', 'COMMENTDELIM','COMMENTSLINE', 'SINGLEQUOTE', 'DOUBLEQUOTE', 'BACKSLASH',
    # Relational Operators: < > <= >=
    'LT', 'GT', 'LEQ', 'GEQ',
    # Equality Operators == !=
    'EQ', 'NE',
    # Delimiters: ( ) { } [ ] , ; :
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'COMMA', 'TERMINATOR', 'COLON',
    # Logical Operators: & ^ | && ||
    'AND', 'XOR', 'OR', 'CONAND', 'CONOR'
    
] + list(reserved.values())

t_ignore = ' \t\x0c '

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENTSLINE(t):
    r'\/\/.*\n'
    t.lexer.lineno += 1

def t_COMMENTDELIM(t):
    r' /\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

t_MEMBERACCESS             = r'\.'
t_INCREMENT         = r'\+\+'
t_DECREMENT        = r'--'
t_TILDE            = r'~'
t_LNOT                = r'!'
t_TIMES            = r'\*'
t_DIVIDE            = r'/'
t_MOD            = r'%'
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_LSHIFT        = r'<<'
t_RSHIFT        = r'>>'
t_LEQ            = r'<='
t_GEQ            = r'>='
t_LT            = r'<'
t_GT            = r'>'
t_EQ            = r'=='
t_NE            = r'!='
t_AND            = r'&'
t_XOR           = r'\^'
t_OR              = r'\|'
t_CONAND        = r'&&'
t_CONOR                = r'\|\|'
t_EQUALS             = r'='
t_PLUSEQUAL           = r'\+='
t_MINUSEQUAL            = r'-='

t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_TERMINATOR  = r';'
t_COLON            = r':'
t_SINGLEQUOTE     = r'\''
t_DOUBLEQUOTE       = r'\"'
t_BACKSLASH       = r'\\'

def t_IDENTIFIER(t):
    r'[a-zA-Z_]([a-zA-Z_0-9])*'
    t.type = reserved.get(t.value,'IDENTIFIER')    #  Check for reserved words
    return t

t_INTCONST = r'\d+'
t_STRCONST = r'\"([^\\\n]|(\\.))*?\"'

t_CHARCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

strinputfile = sys.argv[1]
inputfile = open(strinputfile, 'r')
data = inputfile.read()
lexer.input(data)

tokentype = {}
lexeme = {}            

non_recountable = ['IDENTIFIER']

while True:
    tok = lexer.token()
    if not tok:  
        break     
    tokname = tok.value         
    toktype = tok.type            
    if toktype not in tokentype:        
        tokentype[toktype] = 1         
        lexeme[toktype]=[]              
        lexeme[toktype].append(tokname)  
    else:
        if tokname not in lexeme[toktype]:    
            lexeme[toktype].append(tokname)   
            tokentype[toktype] += 1            
        else:
            if toktype not in non_recountable:   
                tokentype[toktype] +=1            

print("{0:<20s} {1:>5s} {2:>20s}".format("Token", "Occurances", "Lexemes"))
for types in tokentype:
    print("----------------------------------------")
    print("{0:<20s} {1:>5s}".format(types, (str)(tokentype[types])))
    for lexlist in lexeme[types]:
        print("{0:>50s}".format(lexlist))
    print("----------------------------------------")

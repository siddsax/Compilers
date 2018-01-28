#!/usr/bin/python3
import ply.lex as lex
import sys

reserved = {
    'break' : 'BREAK',
    'char' : 'CHAR',
    'continue' : 'CONTINUE',
    # 'foreach' : 'FOREACH',
    # 'in' : 'IN',
    # 'operator' : 'OPERATOR',
    # 'params' : 'PARAMS',
    # 'readonly' : 'READONLY',
    # 'sealed' : 'SEALED',
    # 'static' : 'STATIC',
    # 'this' : 'THIS',
    # 'typeof' : 'TYPEOF',
    # 'unsafe' : 'UNSAFE',
    'void' : 'VOID',
    # 'as' : 'AS',
    # 'byte' : 'BYTE',
    # 'checked' : 'CHECKED',
    # 'decimal' : 'DECIMAL',
    # 'double' : 'DOUBLE',
    # 'explicit' : 'EXPLICIT',
    # 'fixed' : 'FIXED',
    # 'goto' : 'GOTO',
    # 'is' : 'IS',
    'new' : 'NEW',
    # 'out' : 'OUT',
    'private' : 'PRIVATE',
    # 'ref' : 'REF',
    # 'short' : 'SHORT',
    'string' : 'STRING',
    # 'throw' : 'THROW',
    # 'uint' : 'UINT',
    # 'ushort' : 'USHORT',
    # 'volatile' : 'VOLATILE',
    # 'base' : 'BASE',
    # 'case' : 'CASE',
    'class' : 'CLASS',
    # 'default' : 'DEFAULT',
    'else' : 'ELSE',
    # 'extern' : 'EXTERN',
    # 'float' : 'FLOAT',
    'if' : 'IF',
    'int' : 'INT',
    # 'lock' : 'LOCK',
    'null' : 'NULL',
    # 'out' : 'OUT',
    'protected' : 'PROTECTED',
    'return' : 'RETURN',
    'sizeof' : 'SIZEOF',
    # 'struct' : 'STRUCT',
    # 'TRUE' : 'TRUE',
    # 'ulong' : 'ULONG',
    # 'using' : 'USING',
    'while' : 'WHILE',
    # 'bool' : 'BOOL',
    # 'catch' : 'CATCH',
    # 'const' : 'CONST',
    # 'delegate' : 'DELEGATE',
    # 'enum' : 'ENUM',
    # 'FALSE' : 'FALSE',
    # 'for' : 'FOR',
    # 'implicit' : 'IMPLICIT',
    # 'interface' : 'INTERFACE',
    # 'long' : 'LONG',
    'object' : 'OBJECT',
    # 'override' : 'OVERRIDE',
    'public' : 'PUBLIC',
    # 'sbyte' : 'SBYTE',
    # 'stackalloc' : 'STACKALLOC',
    # 'switch' : 'SWITCH',
    # 'try' : 'TRY',
    # 'unchecked' : 'UNCHECKED',
    # 'virtual' : 'VIRTUAL'
    'using'  :  'USING'
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
    # Relational Operators: < > <= >=
    'LT', 'GT', 'LEQ', 'GEQ',
    # Equality Operators == !=
    'EQ', 'NE',
    # Logical Operators: & ^ | && ||
    'AND', 'XOR', 'OR', 'CONAND', 'CONOR',
    # Assignment and Lambda Operators: = += -= 
    'EQUALS', 'PLUSEQUAL', 'MINUSEQUAL',
    # Delimiters: ( ) { } [ ] , ; :
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'COMMA', 'STATTERMINATOR', 'COLON',
    # Others: \n // ... \'" | '\"' | '\\' | '\0' '\t' 
    'NEWLINE', 'COMMENTDELIM','COMMENTSLINE', 'SINGLEQUOTE', 'DOUBLEQUOTE', 'BACKSLASH'

] + list(reserved.values())

# Completely ignored characters
t_ignore = ' \t\x0c '

# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENTSLINE(t):
    r'\/\/.*\n'
    t.lexer.lineno += 1

def t_COMMENTDELIM(t):
    r' /\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Operators
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
t_LT            = r'<'
t_GT            = r'>'
t_LEQ            = r'<='
t_GEQ            = r'>='
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

# Delimiters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_STATTERMINATOR  = r';'
t_COLON            = r':'
t_SINGLEQUOTE     = r'\''
t_DOUBLEQUOTE       = r'\"'
t_BACKSLASH       = r'\\'

# Identifiers and Keywords
def t_IDENTIFIER(t):
    r'[a-zA-Z_]([a-zA-Z_0-9])*'
    t.type = reserved.get(t.value,'IDENTIFIER')    #  Check for reserved words
    return t

# Integer literal
# ? is once or none
t_INTCONST = r'\d+'
t_STRCONST = r'\"([^\\\n]|(\\.))*?\"'
#If doing float
# t_INTCONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Character constant 'c' or L'c'
t_CHARCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comments (Only delimited comments)

    
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


#  Build the lexer
lexer = lex.lex()

# File I/O
# Input filename from terminal
strinputfile = sys.argv[1]
inputfile = open(strinputfile, 'r')

#data = "using System; namespace HelloWorld"
#Convert file to string as lexer takes only string inputs.
data = inputfile.read()

#Giving file (in string form) as input to our lexer
lexer.input(data)

#Data Structures for various counts.
#Stores {token_type : token_count} pairs for each token
tokentype = {}

#The key here is the token_type(like IDENTIFIER, INT, etc.). Value is a LIST of lexemes that match the token.
lexeme = {}            

#This stores those token types which are not be recounted of they occur more than once. For example, a variable name.
non_recountable = ['IDENTIFIER']
#Tokenize input!
while True:
    tok = lexer.token() #Get token
    if not tok:            #No token?
        break      # No more input
    tokname = tok.value         #store the lexeme
    toktype = tok.type             #stores the token_type
    if toktype not in tokentype:        
        tokentype[toktype] = 1            #initianlize count of token to 1
        lexeme[toktype]=[]                #initialize the list in the lexeme dictionary
        lexeme[toktype].append(tokname)    #append lexeme to the lexeme dictionary
        # print(tokname+"\t"+toktype+"NOT here previously")
    else:
        if tokname not in lexeme[toktype]:    
            lexeme[toktype].append(tokname)        #if not present add. above check avoids repetitions
            tokentype[toktype] += 1            #add another token seen of that type
        else:
            if toktype not in non_recountable:            #if this token type is not to be recounted
                tokentype[toktype] +=1            #add token seen.

# print(tokentype)
# print(lexeme)

#printing the tokens
print("{0:<20s} {1:>5s} {2:>20s}".format("Token", "Occurances", "Lexemes"))
for types in tokentype:
    print("----------------------------------------")
    print("{0:<20s} {1:>5s}".format(types, (str)(tokentype[types])))
    for lexlist in lexeme[types]:
        print("{0:>50s}".format(lexlist))
    print("----------------------------------------")

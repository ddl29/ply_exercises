tokens  = (
    'NUM',
    'PLUS',
    'MINUS',
    'IF',
    'ELSE',
    'FI',
    'WHILE',
    'DO',
    'OD',
    'LPAREN',
    'RPAREN', 
    "SEMI", 
    "BEGIN", 
    "END",
    "ASSIGN",
    "ID",
)

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_SEMI = r'\;'
t_ASSIGN = r'\='
t_IF = r'if'
t_ELSE = r'else'
t_FI = r'fi'
t_WHILE = r'while'
t_DO = r'do'
t_OD = r'od'
t_BEGIN = r'begin'
t_END = r'end'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUM(t):
    #if (t[0] == '('):
    #    r'\(*\d+\)*'
    #    try:
    #        t.value = int(t[1:-1])
    #    except ValueError:
    #        print("Integer value too large %d", t.value)
    #        t.value = 0
    #    return t
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
import ply.lex as lex
lexer = lex.lex()

# Definición de la gramática
def p_stmt(t):
    '''stmt : ID ASSIGN LPAREN e RPAREN
            | IF LPAREN e RPAREN stmt ELSE stmt FI
            | IF LPAREN e RPAREN stmt FI
            | WHILE LPAREN e RPAREN DO stmt OD
            | BEGIN stmts END
            '''

def p_stmts(t):
    '''stmts : stmts SEMI stmt
             | stmt'''

def p_e(t):
    '''e : e PLUS t
         | e MINUS t
         | t'''

def p_t(t):
    '''t : ID
         | NUM'''

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


#f = open("./entrada.txt", "r")
#input = f.read()

#print(input)
#parser.parse(input)

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
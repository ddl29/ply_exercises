reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'fi' : 'FI',
    'while' : 'WHILE',
    'do' : 'DO',
    'od' : 'OD',
    'begin' : 'BEGIN',
    'end' : 'END',
}

tokens = [
    'NUM',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN', 
    "SEMI", 
    "ASSIGN",
    "ID",
 ] + list(reserved.values())

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

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID') 
    return t

def t_NUM(t):
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
    print("Error lexico en '%s'" % t.value[0])
    t.lexer.skip(1)
    
import ply.lex as lex
lexer = lex.lex()

# Definición de la gramática
def p_stmt(t):
    '''stmt : ID ASSIGN e
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
         | NUM
         | MINUS ID
         | MINUS NUM'''

def p_error(t):
    if(t == None):
        print("Error sintáctico")
    else:
        print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('input > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
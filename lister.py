tokens = (
    'LIST',
    'LPAREN',
    'RPAREN',
    'OPERANDS',
    'NUM',
)

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUM = r'\d+'
t_OPERANDS = r'\d+\d*'
t_LIST = r'\([\s*\d+\s*]\)'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
import ply.lex as lex
lexer = lex.lex()

#Definición de la gramática
def p_start(t):
    'start : LIST'

def p_list(t):
    '''
    list : LPAREN OPERANDS RPAREN
         | NUM
    '''
    print(len(t[2]))

def p_operands(t):
    '''
    operands : OPERANDS LIST
             | LIST
    '''


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
        s = input('lister > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
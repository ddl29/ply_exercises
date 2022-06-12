tokens = ('LPAREN',
    'RPAREN',
    'NUM',
)

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'

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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
import ply.lex as lex
lexer = lex.lex()

#Definición de la gramática



def p_start(t):
    'start : list'
    #print("start")
    #for i in range(10):
    #    try:
    #        print(i, t[i])
    #    except:
    #        continue

def p_list(t):
    'list : LPAREN operands RPAREN'
    #print("list")
    #for i in range(10):
    #    try:
    #        print(i, t[i])
    #    except:
    #        continue
    

def p_list_num(t):
    'list : NUM'
    #print("list_num")
    #for i in range(10):
    #    try:
    #        print(i, t[i])
    #    except:
    #        continue

def p_operands(t):
    'operands : operands list'
    #print("operands")
    #for i in range(10):
    #    try:
    #        print(i, t[i])
    #    except:
    #        continue

def p_operands_list(t):
    'operands : list'
    #print("operands")
    #for i in range(10):
    #    try:
    #        print(i, t[i])
    #    except:
    #        continue

def p_error(t):
    try:
        print("Error sintáctico en '%s'" % t.value)
    except:
        print("Error sintáctico incalculable")

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
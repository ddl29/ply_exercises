tokens = ('LPAREN',
    'RPAREN',
    'NUM',
)

counts = []

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
##
#def t_NUM(t):
#    r'\d+'
#    try:
#        t.value = int(t.value)
#    except ValueError:
#        print("Integer value too large %d", t.value)
#        t.value = 0
#    return t
##
t_NUM = r'[0-9_][0-9_]*'
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
from queue import Empty
import ply.lex as lex
lexer = lex.lex()



#Definición de la gramática

def p_start(t):
    'start : list'
    '''print("start")
    for i in range(10):
        try:
            print(i, t[i])
        except:
            continue'''
    
    #print("counts:", counts)
    if len(counts) > 2:
        tmp = counts[-2]
        counts[-2] = counts[-1]
        counts[-1] = tmp
    print("counts:", counts)


    counts.clear()
    return t

def p_list(t):
    'list : LPAREN operands RPAREN'
    
    '''print("list")
    for i in range(10):
        try:
            print(i, t[i])
        except:
            continue'''
    #print("")
    return t

def p_list_num(t):
    'list : NUM'
    '''if t[1] == '1':
        print("Encontre un num")
        counts[-1] += 1
    '''
    #t[0] = 1
    if counts:
        counts[-1] += 1
    '''print("list_num")
    for i in range(10):
        try:
            print(i, t[i])
        except:
            continue'''
    #print("")
    return t

def p_operands(t):
    'operands : operands list'
    #if t[0] != None:
    #    t[0] += 1
    '''print("operands")
    for i in range(10):
        try:
            print(i, t[i])
        except:
            continue
    print("")'''
    return t

def p_operands_list(t):
    'operands : list'
    #t[0] = 1
    counts.append(1)
    
    '''print("operands_list")
    for i in range(10):
        try:
            print(i, t[i])
        except:
            continue
    print("")'''
    return t



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
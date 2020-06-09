#Funciones matemáticas de potenciación

from math import sqrt as ra

def potencia(b,e):   #b^e
    return b**e
def potCadena(b,e,v):   #(b^e)^(b^e)^(b^e)^(b^e)^..... 'v' veces
    r=0
    r=b**e
    while v>0:
        r=r**r
        v-=1
    return r
def potEscalera(b,e,v): #(((((((((b^e)^e)^e)^e)^e)^e)^e)^e)^e)... 'v' veces
    return potencia(b,potCadena(e,e,v))
def raiz2(num):
    return ra(num)
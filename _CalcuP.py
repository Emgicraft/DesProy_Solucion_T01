#Programa de Prueba de una calculadora con múltiples funciones

from math import pi

import _FuncionesExtras as fe

import LibCalcuP.fun_pot as Lfp

import LibCalcuP.Funciones_especiales.trigonometricas_inversas as LFetrI

print(fe.factorialN(7))
print(Lfp.potencia(2,4))
print(LFetrI.asen(0.5))

cartesiana=str(input("Ingrese coordenadas cartesianas: "))

cart=cartesiana.split(" ")

x = y = z = rc = re = tetaC = tetaE = fi = 0.0

#elec=int(input("1-Cilindrica  2-Esféricas  Qué elije? "))

x, y, z = float(cart[0]), float(cart[1]), float(cart[2])

if len(cart)==3:
    #Calculo coordenadas cilindricas:
    rc=Lfp.raiz2(Lfp.potencia(x,2)+Lfp.potencia(y,2))
    tetaC=LFetrI.atan(y/x)
    tetaC=(tetaC*180)/pi
    
    #Calculo coordenadas esféricas:
    re=Lfp.raiz2(Lfp.potencia(x,2)+Lfp.potencia(y,2)+Lfp.potencia(z,2))
    tetaE=LFetrI.atan(y/x)
    tetaE=(tetaE*180)/pi
    fi=LFetrI.acos(z/re)
    fi=(fi*180)/pi

    print("""
Coordenadas Cilindricas:
r=%s
teta=%s
z=%s

Coordenadas Esféricas:
r=%s
teta=%s
fi=%s
    """%(rc,tetaC,z,re,tetaE,fi))
else:
    print("Error, no ingreso tres coordenadas.")

"""
base=float(input("\nBase: "))
expo=int(input("Potencia: "))
#cont=1
cntB=base
#while cont<expo:
#    cont+=1
#    base=cntB*base
#print("ResW.: ",base)
for i in range(expo-1):
    base=cntB*base
print("ResF.: ",base)

a, b, c = 0, 1, 0
n=int(input("\nN="))

#print(a)
#print(b)
for i in range(n):
    c=a+b
    print(a)
    a, b = b, c"""
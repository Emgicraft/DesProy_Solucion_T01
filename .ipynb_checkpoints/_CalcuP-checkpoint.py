#Programa de Prueba de una calculadora con múltiples funciones

from math import pi

import _FuncionesExtras as fe

import LibCalcuP.fun_pot as Lfp

import LibCalcuP.Funciones_especiales.trigonometricas_inversas as LFetrI

print(fe.factorialN(7))
print(Lfp.potencia(2,4))
print((LFetrI.asen(0.5)*180)/pi)

fe.fibonacci(17)


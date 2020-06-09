#Funciones matemáticas adicionales

def dividir(x,y):
	if y!=0:
		return (x/y)
	else:
		return 0
def factorialN(x):
	res=x
	while x>1:
		res=res*(x-1)
		x=x-1
	if x>=0:
		return res
	else:
		print("Valor inválido, número negativo ingresado.")
		return 0
def combinatoria(n,x):
	if n>=x:
		return dividir(factorialN(n),factorialN(x)*factorialN(n-x))
	else:
		return 0

""""
def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios, **k):
    print(parametro_fijo)
    for arg in arbitrarios:
        print(arg)
    # Los argumentos arbitrarios tipo clave, se recorren como los diccionarios
    for c in k:
        print("El valor de", c, "es", k[c])
recorrer_parametros_arbitrarios("Fixed", "arbitrario 1", 16.84, "arbitrario 3", clave1=3.15, clave2="valor dos")

def calcular(importe, descuento):
 return importe - (importe * descuento / 100)
datos = [1500, 10]

print(calcular(*datos))
"""
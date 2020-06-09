#Funciones matemáticas básicas

def sumar(x,y):
	return (x+y)
def restar(x,y):
	return (x-y)
def multiplicar(x,y):
	return (x*y)
def dividir(x,y):
	if y!=0:
		return (x/y)
	else:
		print("Error! Denominador igual a 0")
		return 0
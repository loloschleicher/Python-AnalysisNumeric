import math
import sympy 
from sympy import Symbol

#valor del Xi
xi = 1

#valor del Xi+1
xiMasUno = 2

#valor del incremento
h = xiMasUno - xi

#determinar cual va aser la variable para la deriavada (se usa en la funcion diff)
x = Symbol('x')

#Determinamos la funcion
funcion = 25*(x**3) - (6*(x**2)) + (7*x) - 88

#Calcular valor verdadero
valorverdadero = (25 * math.pow(xiMasUno , 3)) - (6 * math.pow(xiMasUno , 2)) + (7 * xiMasUno) - 88

#este valor se va a usar para los factoriales y exponenciales de h
orden = 0 

aux = 0

#iterar desde la orden 0 hasta la 3
while orden <= 3:

    #En esta variable se van a ir calculando los diferentes resultados segun el numero de orden, la funcion diff se usa para derivar en pythnon, esta reibe la funcion
    #a derivar, la/las variable/s y el orden de la derivada..la funcion subs reemplaza la variable x por un valor real
    fxiMasUno = aux + ((sympy.diff(funcion, x, orden).subs(x, xi))/math.factorial(orden) ) * h**orden

    #Ir guardando el resultado de la  orden anterior para poder usarlo en la proxima orden
    aux = fxiMasUno

    #calcular el error en cada aproximacion
    errorRelativoporcentual = ((valorverdadero - aux) / valorverdadero) * 100

    print("El error en el orden " + str(orden) + " es: " + str(errorRelativoporcentual))

    orden += 1



print("El valor verdadero es: " + str(valorverdadero))
print("El valor aproximado hasta el orden 3 es: " +str(aux))



    
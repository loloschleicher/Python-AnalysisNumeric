import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot

#definir la funcion que se desea calcular la raiz
def f(x):
    funcion = 5*x**3 - 5*x**2 + 6*x -2 
    return funcion


def grafica():
    #determinar el rango de valores de x
    x = range(-10, 10)
    #para cada valor de x voy asignadole un valor de y (para eso voy invocando a la funcion y le voy pasando los valores de x)
    pyplot.plot(x, [f(i) for i in x])
    #definir los colores de os ejes
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    #Limitar los valores de los ejes.
    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)
    #Guardar gráfico como imágen PNG.
    pyplot.savefig("output.png")
    #Mostrarlo.
    pyplot.show()


def biseccion(xl, xu):
    #Definir el porcentaje de error
    Es = 10

    #Declarar el xr anterior = 0
    xrAnt = 0
    
    #hacer una primera iteracion para calcular la raiz
    xrSig = (xl + xu) / 2

    #Calcular el error aproximado
    Ea = abs(((xrSig - xrAnt) / xrSig) * 100)

    #comprobar si el error aproximado es menor o igual que el Es entonces ya se encontro encontro el valor de la raiz
    if Ea <= Es:
        print("El error en la iteracion 0 es: " + str(Ea))
        print("EL valor es de la raiz es: " + str(xrSig))
        
    #declaro para contar las cantidades de iteraciones solamente   
    i=0

    #mientras el valor sea distinto de cero no se encontro el valor de la raiz, entonces sigue iterando 
    while Ea > Es:

        #volver a calcular la raiz 0.5
        xrSig = (xl + xu) / 2

        #Calcular el error aproximado
        Ea = abs(((xrSig - xrAnt) / xrSig) * 100)

        #ir imprimendo el error en cada iteracion
        print("El error en la iteracion " + str(i) + " es: " + str(Ea))

        #volver a comprobar el valor para saber si es menor o mayor a cero
        valor = f(xrSig) * f(xl)

        #si es menor a cero enotnces la raiz esta del lado de menor valor del intervalo
        if valor < 0:
            xu = xrSig
        #de lo contrario la raiz esta del lado de mayor valor del intervalo
        else:
            xl = xrSig

        #Actualizar el xr anterior por el xr siguiente
        xrAnt = xrSig
        i += 1

    print("El valor de la raiz es: " + str(xrSig))

print("\nGrafica")
grafica()
print("\nMetodo de Biseccion: ")
xl = float(input("Ingrese el menor valor del intervalo"))
xu = float(input("Ingrese el mayor valor del intervalo\n"))
print("\n")
biseccion(xl,xu)

#El problema pide hallar la raiz mas pequenia, pero esta funcion tiene una sola raiz



    


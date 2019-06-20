import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot

#definir la funcion que se desea calcular la raiz
def f(x):
    funcion = -0.5*x**2 + 2.5*x +4.5 
    return funcion


def grafica():
    #determinar el rango de valores de x
    x = range(-10, 15)
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


def resolvente(a, b, c):
    #comprobar si la funcion es lineal
    if a == 0:
        x = - (c/b)
        return print("El valor de la raiz de la funcion lineal es: " + str(x))
    
    #calcular el discriminante (valor dentro de la raiz)
    discriminante = b*b-4*a*c 
    
    # Si el discriminante es mayor a 0 entonces tiene dos soluciones
    if discriminante > 0:
        
       #calcular las dos soluciones e imprimir
       solucion1 = (-b + math.sqrt(discriminante)) / (2 * a)
       solucion2 = (-b - math.sqrt(discriminante)) / (2 * a)
       print("\n Tiene dos posibles soluciones: \n x1 = " + str(solucion1) + "\n x2 = " + str(solucion2))
   
    # Si el discriminante es igual a 0 entonces tiene una unica solucion
    else:
        if discriminante == 0:
            solucion = -b / (2 *a)
            print("\n Tiene una unica solucion: \n x = " + str(solucion))
        
        #Sino si el discriminante es menor a 0 entonces es un numero complejo
        else:
            # i^2 = -1, entonces i = raiz de -1
            # cualquier raiz cuadrada de un numero negativo puede descomponerse como la raiz cuadra del numero en positivo * por la raiz cuadra de -1
            # entonces la resolucion es simplemente resolver la raiz cuadrada del numero negativo (pero pasado a positivo) y se le agrega el i de imaginario
            
            #pasar el discriminante de negativo a positivo para poder resolver la raiz
            discAbsoluto = -discriminante
            
            #resolver la raiz cuadrada del discriminante para obtener el numero imaginario
            imaginario = math.sqrt(discAbsoluto)
            
            #calcular la division del termino real de la resta de x1
            terminoRealX1 = (-b/(2*a))  
            
            #calcular la division del termino imaginario de la resta de x1
            terminoImagX1 = ((-imaginario)/(2*a))
            
            #imprimir el termino real y el termino imaginario de x1
            print('x1 = ' + str(terminoRealX1) + ' ' + ' ' + str(terminoImagX1) + 'i')
            
            #calcular la division del termino real de la suma de x2
            terminoRealX2 = (-b/(2*a))  
            
            #calcular la division del termino imaginario de la suma de x2
            terminoImagX2 = ((imaginario)/(2*a))
            
            #imprimir el termino real y el termino imaginario de x2
            print('x2 = ' + str(terminoRealX2) + ' + ' + str(terminoImagX2) + 'i')
            
           


def biseccion(xl, xu):
    #declarar el valor de xr anterior
    xrAnt = 0

    #hacer una primera iteracion para calcular la raiz
    xrSig = (xl + xu) / 2

    #comprobar el valor para saber si es igual o distinto de cero
    valor = f(xrSig) * f(xl)

    Ea = abs(((xrSig - xrAnt) / xrSig) * 100)

    if valor == 0:
        print("El error en la iteracion 0 es: " + str(Ea))
        print("El valor de la raiz mas grande es: " + str(xrSig))

    #variable para contar las cantidades de iteraciones
    i =0
    #mientras el valor sea distinto de cero no se encontro el valor de la raiz, entonces sigue iterando 
    while i <= 3:

        #volver a calcular la raiz
        xrSig = (xl + xu) / 2

        #Calcular el error aprx. en cada iteracion e ir imprimiendo
        Ea = abs(((xrSig - xrAnt) / xrSig) * 100)
        print("El error en la iteracion " + str(i) + " es: " +str(Ea))

        #volver a comprobar el valor para saber si es menor o mayor a cero
        valor = f(xrSig) * f(xl)

        #si es menor a cero enotnces la raiz esta del lado de menor valor del intervalo
        if valor < 0:
            xu = xrSig
        #de lo contrario la raiz esta del lado de mayor valor del intervalo
        else:
            xl = xrSig

        #Ir actualizando el valor de xr anterior por el xr siguiente
        xrAnt = xrSig
        i += 1

    print("El valor de la raiz mas grande es: " + str(xrSig))

print("\nGrafica")
grafica()
print("Resolvente: ")
a = float(input("Ingrese el valor de a: \n"))
b = float(input("Ingrese el valor de b: \n"))
c = float(input("Ingrese el valor de c: \n"))
print("\nMetodo de Biseccion: ")
xl = float(input("Ingrese el menor valor del intervalo"))
xu = float(input("Ingrese el mayor valor del intervalo\n"))
print("\n\nResultado de la Resolvente:")
resolvente(a, b, c) 
print("\nResultado del Metodo de Biseccion:")
biseccion(xl,xu)



    


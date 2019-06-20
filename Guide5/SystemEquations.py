# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:02:09 2019

@author: Juan Carlos
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
import math

#definir la funcion que se desea calcular la raiz
def ecuacionUnoDeXuno(x):
    #Despejar x1
    xUno = (8*x - 24) / 4
    return xUno

#definir la funcion que se desea calcular la raiz
def ecuacionDosDeXuno(x):
    #Despejar x1
    xUno = -6*x + 34
    return xUno

#definir la funcion que se desea calcular la raiz
def ecuacionUnoDeXdos(x):
    #Despejar x2
    xDos = (-4*x - 24) / -8
    return xDos

#definir la funcion que se desea calcular la raiz
def ecuacionDosDeXdos(x):
    #Despejar x2
    xDos = (-x + 34) / 6
    return xDos


#Graficar las ecuaciones uno y dos de x1
def graficaXuno():
    #determinar el rango de valores de x
    x = range(-5, 10)
    #para cada valor de x voy asignadole un valor de y (para eso voy invocando a la funcion y le voy pasando los valores de x)
    pyplot.plot(x, [ecuacionUnoDeXuno(i) for i in x], 'mo-')#Funcion 1 color Violeta
    pyplot.plot(x, [ecuacionDosDeXuno(i) for i in x], 'bo-')#Funcion 2 color azul
    
    
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

#Graficar las ecuaciones uno y dos para x2
def graficaXdos():
    #determinar el rango de valores de x
    x = range(-5, 10)
    #para cada valor de x voy asignadole un valor de y (para eso voy invocando a la funcion y le voy pasando los valores de x)
    pyplot.plot(x, [ecuacionUnoDeXdos(i) for i in x], 'mo-')#Funcion 1 color Violeta
    pyplot.plot(x, [ecuacionDosDeXdos(i) for i in x], 'bo-')#Funcion 2 color azul
    
    
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


def resultadoEcuacionXuno(): 
    n =  - 5
    while n <= 10:
        #ver cuando se intersectan las rectas, entonces ese es el valor de la incognita, despues imprimo cualquiera de los dos valores porque son iguales
        if ecuacionUnoDeXuno(n) == ecuacionDosDeXuno(n):
            print("El valor de x1 = " + str(ecuacionUnoDeXuno(n)))
        n += 1 
        
def resultadoEcuacionXdos():
    n =  - 5
    while n <= 10:
        #ver cuando se intersectan las rectas, entonces ese es el valor de la incognita, despues imprimo cualquiera de los dos valores porque son iguales
        if ecuacionUnoDeXdos(n) == ecuacionDosDeXdos(n):
            print("El valor de x2 = " + str(ecuacionUnoDeXdos(n)))
        n += 1 
#uso de las librerias de python para comprobar valores      
def resolverEcuaciones():
    #declarar la matriz con los valores 
    a = np.array([[4, -8],
               [1, 6]])
    
    #declarar el array de terminos independientes pero en forma traspuesta
    b = np.array([-24, 34])
    
    #la funcion solve() espera la matriz y el array de los terminos independientes y devuelve los valores en el orden: x1,x2...xn 
    x = np.linalg.solve(a, b)
    print("\nLos resultados de x1 y x2 son: " + str(x) + " respectivamente")
    
    #verificar si los resultados son correctos, la funcion dot() devuelve el producto entre dos array o matrices,
    # y la funcion allclose compara el valor entre dos elementos que recibe como parametro, si sn exactos devuelve true
    print("Verificacion: " + str(np.allclose(np.dot(a, x), b)))
        
print("\nGrafica de las ecuaciones de x1")
graficaXuno()
resultadoEcuacionXuno()
print("\nGrafica de las ecuaciones de x2")
graficaXdos()
resultadoEcuacionXdos()
resolverEcuaciones()
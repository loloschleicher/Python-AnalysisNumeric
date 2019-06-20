import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
import math

#definir la funcion despejando x siguiente
def f(x):
    xSig = 2 * math.sin(math.sqrt(x))
    return xSig

#funcion original para graficar 
def fGrafica(x):
    fxi = math.sin(math.sqrt(x)) * 2 - x
    return fxi    


def grafica():
    #determinar el rango de valores de x
    x = range(0, 40)
    #para cada valor de x voy asignadole un valor de y (para eso voy invocando a la funcion y le voy pasando los valores de x)
    pyplot.plot(x, [fGrafica(i) for i in x])
    #definir los colores de os ejes
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    #Limitar los valores de los ejes.
    pyplot.xlim(-10, 10)
    pyplot.ylim(-20, 20)
    #Guardar gráfico como imágen PNG.
    pyplot.savefig("output.png")
    #Mostrarlo.
    pyplot.show()



def puntoFijo(x):
    #Definir el porcentaje de error
    Es = 0.001

    #Declarar el xr anterior = 0
    xAnt = x
    
    #Calcular el x siguiente
    f(x)
 

    #Calcular el error aproximado
    Ea = abs(((f(x) - xAnt) / f(x)) * 100)

    #comprobar si el error aproximado es menor o igual que el Es entonces ya se encontro encontro el valor de la raiz
    if Ea <= Es:
        print("El error en la iteracion 0 es: " + str(Ea))
        print("EL valor es de la raiz es: " + str(f(x)))
        
    #declaro para contar las cantidades de iteraciones solamente   
    i = 0
    #mientras el error aproximado sea mayor al Es entonces sigue iterando 
    while Ea > Es:

        #Calcular el error aproximado..la funcion f recibe siempre el valor anterior para calcular el siguiente
        Ea = abs(((f(xAnt) - xAnt) / f(xAnt) * 100))
        
        #ir imprimendo el error en cada iteracion
        print("El error en la iteracion " + str(i) + " es: " + str(Ea))
        
        #Almaceno el valor de x siguiente en x anterior para luego pasarlo como parametro a la funcion f
        xAnt = f(xAnt)
        
        i+=1
            

    print("El valor de la raiz es: " + str(f(xAnt)))

grafica()
x = float(input("Ingrese el valor inicial"))
print("\n")
print("Metodo Del punto Fijo: ")
puntoFijo(x)


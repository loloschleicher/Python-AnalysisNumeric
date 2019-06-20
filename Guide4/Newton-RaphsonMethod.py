import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
import sympy 
import math
from sympy import Symbol


#definir la funcion que se desea calcular la raiz
def fn(xi):
    x = Symbol('x')
    fxiDeriv = 0.5*x**3 -4*x**2 + 5.5*x -1
    fxi = 0.5*xi**3 -4*xi**2 + 5.5*xi -1
    derivadaFxi = sympy.diff(fxiDeriv, x).subs(x, xi) 
    xSig = xi - (fxi / derivadaFxi)
    return xSig

def f(xi):
    fxi = 0.5*xi**3 -4*xi**2 + 5.5*xi -1
 
    return fxi    


def grafica():
    #determinar el rango de valores de x
    x = range(-20, 20)
    #para cada valor de x voy asignadole un valor de y (para eso voy invocando a la funcion y le voy pasando los valores de x)
    pyplot.plot(x, [f(i) for i in x])
    #definir los colores de os ejes
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    #Limitar los valores de los ejes.
    pyplot.xlim(-15, 17)
    pyplot.ylim(-20, 20)
    #Guardar gráfico como imágen PNG.
    pyplot.savefig("output.png")
    #Mostrarlo.
    pyplot.show()


def newton(xi):
    #Definir el porcentaje de error
    Es = 0.01

    #Declarar el xr anterior = 0
    xAnt = xi
    
    #Calcular el x siguiente
    fn(xi)
    

    #Calcular el error aproximado
    Ea = abs(((fn(xi) - xAnt) / fn(xi)) * 100)

    #comprobar si el error aproximado es menor o igual que el Es entonces ya se encontro encontro el valor de la raiz
    if Ea <= Es:
        print("El error en la iteracion 0 es: " + str(Ea))
        print("EL valor es de la raiz es: " + str(fn(xi)))
        
    #declaro para contar las cantidades de iteraciones solamente   
    i = 0
    #mientras el error aproximado sea mayor al Es entonces sigue iterando 
    while Ea > Es:

        #Calcular el error aproximado..la funcion fn recibe siempre el valor anterior para calcular el siguiente
        Ea = abs(((fn(xAnt) - xAnt) / fn(xAnt) * 100))
        
        #ir imprimendo el error en cada iteracion
        print("El error en la iteracion " + str(i) + " es: " + str(Ea))
        
        #Almaceno el valor de x siguiente en x anterior para luego pasarlo como parametro a la funcion f
        xAnt = fn(xAnt)
        
        i+=1
            

    print("El valor de la raiz es: " + str(fn(xAnt)))


print("\nGrafica")
grafica()
print("\nMetodo de Newton - Raphson: ")
xi = float(input("Ingrese el valor inicial"))
newton(xi)



    




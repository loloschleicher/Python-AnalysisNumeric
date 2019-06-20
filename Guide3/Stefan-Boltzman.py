import math
import sympy 
from sympy import Symbol

def Boltzman(e, A, T, deltaT1, deltaT2):

    #constante de Boltzman
    o = 5.67e-8

    #determinar cual va aser la variable para la deriavada (se usa en la funcion diff)
    x = Symbol('x')

    #Crear la fncion de Boltzman reemplazando T por x para usar como variable para derivar
    H = e*o*A*x**4

    valorVerdadero = (e*o*A*T**4)

    #Calcular la derivada primera de la funcion de Boltzman
    derivada = sympy.diff(H, x).subs(x, T)

    #Calculo con el primer delta
    
    #Calcular el valor mediante la formula de propagacion de errores
    valor = derivada * deltaT1

    #Calculo del error
    error = valor/valorVerdadero * 100

    print("\n\n----------------Resultado con variacion Temperatura = ± " + str(deltaT1) + "---------------- \n")

    print("El valor verdadero H = " + str(valorVerdadero) + " varia con un △ H = ± " + str(valor) + " Cuando la temperatura absoluta varia ± en " + str(deltaT1))

    print("\nEl error es: " + str(error) + "%\n\n")



    #Calculo con el segundo delta

    #Calcular el valor mediante la formula de propagacion de errores
    valor = derivada * deltaT2

    #Calculo del error
    error = valor/valorVerdadero * 100

    print("\n\n-------------------Resultados con variacion de Temperatura = ± " + str(deltaT2) + "------------------- \n")

    print("El valor verdadero H = " + str(valorVerdadero) + " varia con un △ H = ± " + str(valor) + " Cuando la temperatura absoluta varia en ± " + str(deltaT2))

    print("\nEl error es: " + str(error) + "%\n\n")
    


e = float(input("Ingrese el valor de la emisividad:"))
A = float(input("Ingrese el valor del area:"))
T = float(input("Ingrese el valor de la temperatura:"))
deltaT1 = float(input("Ingrese el valor de la primer variacion de la temperatura (sin signos):"))
deltaT2 = float(input("Ingrese el valor de la segunda variacion de la temperatura (sin signos):"))
Boltzman(e, A, T, deltaT1, deltaT2)

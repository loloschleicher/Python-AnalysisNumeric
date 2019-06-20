# -*- coding: utf-8 -*-
"""
Created on Mon May 13 02:13:53 2019

@author: Schleicher Leonel
"""
from colorama import init, Fore, Back, Style
from sympy import *
from sympy import Symbol
from sympy import integrate
import math

#formula de la regla del trapecio compuesta (b - a) * n [(f(a) + f(b) / 2) + sumatoria f(a + k * h)] sumatoria va desde k=1 hasta n-1
def trapecio(func, a, b, n):
    # evaluar la funcion en f(a) y en f(b) 
    fAmasFb = eval(func.replace("x", "(a)")) + eval(func.replace("x", "(b)"))
    
    # Si n = 1 entonces se trata de la regla del trapecio simple por ende devuelve ese valor la funcion    
    if n == 1:
        return (b - a) * (fAmasFb / 2)
    
    #de lo contrario, calcular h (el ancho uniforme de los intervalos)
    h = (b-a) / n
        
    sumatoria = 0
    #hacer la sumatoria de la funcion evaluada desde k = 1 hasta n-1
    k = 1
    while k <= n-1:       
        sumatoria += eval(func.replace("x", "(a + k * h)"))#replace(se reemplaza la x de la funcion por un valor que uno desea) y eval() evalua la funcion con ese valor
        k += 1
    
    #devolver el valor del area integrada segun la fotmula del trapecio multiple     
    return h * ((fAmasFb / 2) + sumatoria)


def simpsonUnTercio(func, a, b, n, desicion):
    # evaluar la funcion en f(a) y en f(b) 
    fAmasFb = eval(func.replace("x", "(a)")) + eval(func.replace("x", "(b)"))
    
    if desicion == 2:
        fXuno = eval(func.replace("x", "(n)"))
        return ((b - a) / 6) * (fAmasFb + (4 * (fXuno) ))
    # Si n = 2 entonces se trata de la regla de simpson 1/3 simple por ende devuelve ese valor la funcion    
    if n == 2:
        #calcular la funcion evaluada en f(a + b / 2) que se usaria en el caso de  que n es igual a 2
        fXuno = eval(func.replace("x", "(a + ( b - a ) / 2)"))
        return ((b - a) / 6) * (fAmasFb + (4 * (fXuno) ))
    
    #de lo contrario, calcular h (el ancho uniforme de los intervalos)
    h = (b-a) / n
        
    sumatoriaI = 0
    #hacer la sumatoria de la funcion evaluada desde i = 0 hasta n-1
    i = 1
    while i <= n-1:       
        sumatoriaI += eval(func.replace("x", "(a + i * h)"))#replace(se reemplaza la x de la funcion por un valor que uno desea) y eval() evalua la funcion con ese valor
        i += 2
        
    sumatoriaJ = 0
    #hacer la sumatoria de la funcion evaluada desde j = 2 hasta n-2
    j = 2
    while j <= n-2:       
        sumatoriaJ += eval(func.replace("x", "(a + j * h)"))#replace(se reemplaza la x de la funcion por un valor que uno desea) y eval() evalua la funcion con ese valor
        j += 2
    
    
    #devolver el valor del area integrada segun la regla de simpson 1/3 multiple      
    return (h/3) * ((fAmasFb) + (4 * sumatoriaI) + (2 * sumatoriaJ))




def simpsonTresOctavos(func, a, b, n, relleno, desicion):
    # evaluar la funcion en f(a) y en f(b) 
    fAmasFb = eval(func.replace("x", "(a)")) + eval(func.replace("x", "(b)"))
    
    if desicion == 2:
        #calcular la funcion evaluada en f(2 * a + b / 3) que se usaria en el caso de  que n es igual a 3
        fXuno = eval(func.replace("x", "(n)"))
        
        #calcular la funcion evaluada en f(a + 2 * b / 3) que se usaria en el caso de  que n es igual a 3
        fXdos = eval(func.replace("x", "(relleno)"))
        return ((b - a)  / 8) * (fAmasFb + (3 * fXuno) + (3 * fXdos))
        
    # Si n = 3 entonces se trata de la regla de simpson 8/3 simple por ende devuelve ese valor la funcion    
    if n == 3:
        #calcular la funcion evaluada en f(2 * a + b / 3) que se usaria en el caso de  que n es igual a 3
        fXuno = eval(func.replace("x", "(a + ((b - a) / 3))"))
        
        #calcular la funcion evaluada en f(a + 2 * b / 3) que se usaria en el caso de  que n es igual a 3
        fXdos = eval(func.replace("x", "((a + ((b - a) / 3)) + (b-a) / 3)"))
        return ((b - a)  / 8) * (fAmasFb + (3 * fXuno) + (3 * fXdos))
    
    #de lo contrario, calcular h (el ancho uniforme de los intervalos)
    h = (b-a) / n
        
    sumatoriaI = 0
    #hacer la sumatoria de la funcion evaluada desde i = 1 hasta n-2 con saltos de 3

    i = 1
    while i <= n-1:       
        sumatoriaI += eval(func.replace("x", "(a + i * h)"))#replace(se reemplaza la x de la funcion por un valor que uno desea) y eval() evalua la funcion con ese valor
        i += 3
        
    sumatoriaJ = 0
    #hacer la sumatoria de la funcion evaluada desde j = 2 hasta n-1 con saltos de 3
    j = 2
    while j <= n-2:       
        sumatoriaJ += eval(func.replace("x", "(a + j * h)"))#replace(se reemplaza la x de la funcion por un valor que uno desea) y eval() evalua la funcion con ese valor
        j += 3
        
    sumatoriaK = 0
    #hacer la sumatoria de la funcion evaluada desde k = 3 hasta n-3 con saltos de 3
    k = 3
    while k <= n-3:       
        sumatoriaK += eval(func.replace("x", "(a + k * h)"))#replace(se reemplaza la x de la funcion por un valor que uno desea) y eval() evalua la funcion con ese valor
        k += 3 
    
    #devolver el valor del area integrada segun la regla de simpson 3/8 multiple      
    return ((3/8) * h) * ((fAmasFb) + (3 * sumatoriaI) + (3 * sumatoriaJ) + (2 * sumatoriaK))


#algoritmo implementado del pseudocodigo de Chapra pagina 642 Figura 21.15 b)
def intervalosDesiguales(func, intervalos):
    h = intervalos[1] - intervalos[0]
    k = 1
    j = 1
    suma = 0
    for j in range(1, len(intervalos)):
        #este if solo se ejecuta si esta en el ultimo elemento el ciclo for, se usa para corregir el problema de desboradamiento porque el for no puede leer el j+1 cuando esta en el ultimo elemento
        if j == (len(intervalos) - 1):
            hf = intervalos[j] - intervalos[j-1]
            h = intervalos[j-2] - intervalos[j-1]
        else:
            hf = intervalos[j+1] - intervalos[j]
        
        if abs(h - hf) < .000001: # se compara si los intervalos adyacentes son iguales
            if k == 3: 
                suma += simpsonUnTercio(func, intervalos[j-3], intervalos[j-1],intervalos[j-2], 2)
                k -= 1
            else:
                k += 1
        else:
            if k == 1:
                suma += trapecio(func, intervalos[j-1], intervalos[j], 1)
            else:
                if k == 2:
                    suma += simpsonUnTercio(func, intervalos[j-2],intervalos[j],intervalos[j-1], 2)
                    
                else:
                    suma += simpsonTresOctavos(func, intervalos[j-3],intervalos[j],intervalos[j-2],intervalos[j-1], 2)
                k = 1
        h = hf        
    return suma



# integral para calcular el valor verdaderode la funcion
def integVerdadera(func, a, b):
    x = Symbol('x')
    return integrate(func, (x,a,b))# la funcion integrate de sympy recibe como argumento una funcion y el intervalo de integracion

print(f"\n{Fore.RED}IMPORTANTE: \n*PARA EL NUMERO 'e' DEBE INGRESAR EL VALOR NUMERICO (2.71828) sino ingrese 'E'{Style.RESET_ALL}")
func = input("ingerese la funcion ej: 1-E**(-2*x): ")
desicion = int(input("Si desea calcular para intervalos iguales presione 1, de lo contrario 2: "))
if desicion == 1:
    a = float(input("ingerese el inicio del intervalo (a) : "))
    b = float(input("ingerese el final del intervalo (b) : "))
    desicionUno = int(input("Si quiere calcular por regla del trapecio presione 1, por regla Simpson 1/3 presione 2, por regla Simpson 3/8 presione 3: "))   
    if desicionUno == 1:
        print(f"\n{Fore.RED}IMPORTANTE: \n*PARA REGLA DEL TRAPECIO SIMPLE EL VALOR DE 'n' DEBE SER 1{Style.RESET_ALL}")
        n = abs(float(input("ingerese el numero de divisiones (n) : "))) 
        while n == 0:
            n = abs(float(input("n debe ser distinto de 0, ingrese de nuevo: "))) 
     
        print("\nEl valor del area por regla del trapecio es: ", abs(trapecio(func, a, b, n)), " unidades de area")

        print("El valor verdadero del area es: ", abs(integVerdadera(func, a, b)), " unidades de area")

        # calcular e imprimir el error relativo porcentual
        print("El error relativo porcentual verdadero es del: ", abs(((integVerdadera(func, a, b) - trapecio(func, a, b, n)) / integVerdadera(func, a, b))) * 100, " %")

        print("El error absoluto es: ", abs(integVerdadera(func, a, b) - trapecio(func, a, b, n)), " unidades de area")
    
    elif desicionUno == 2:
        print(f"\n{Fore.RED}IMPORTANTE:\n*PARA REGLA DE SIMPSON 1/3 SIMPLE EL VALOR DE 'n' DEBE SER 2{Style.RESET_ALL}")
        n = abs(float(input("ingerese el numero de divisiones (n) : "))) 
        while (n%2) != 0 or n == 0 or n == 1:
            n = abs(float(input("n debe ser numero par y distinto de 0 y de 1, ingrese de nuevo: "))) 
        
        print("\nEl valor del area por regla de Simpson 1/3 es: ", abs(simpsonUnTercio(func, a, b, n, desicion)), " unidades de area")

        print("El valor verdadero del area es: ", abs(integVerdadera(func, a, b)), " unidades de area")

        # calcular e imprimir el error relativo porcentual
        print("El error relativo porcentual verdadero es del: ", abs(((integVerdadera(func, a, b) - simpsonUnTercio(func, a, b, n, desicion)) / integVerdadera(func, a, b))) * 100, " %")

        print("El error absoluto es: ", abs(integVerdadera(func, a, b) - simpsonUnTercio(func, a, b, n, desicion)), " unidades de area")
        
    elif desicionUno == 3:
        print(f"\n{Fore.RED}IMPORTANTE:\n*PARA REGLA DE SIMPSON 3/8 SIMPLE EL VALOR DE 'n' DEBE SER 3{Style.RESET_ALL}")
        n = abs(float(input("ingerese el numero de divisiones (n) : "))) 
        while n == 0 or n == 1 or n == 2 or n%2 == 0:
            n = abs(float(input("n debe ser numero impar y distinto de 0, de 1 y de 2, ingrese de nuevo: "))) 
        
        print("\nEl valor del area por regla de Simpson 3/8 es: ", abs(simpsonTresOctavos(func, a, b, n, 0, desicion)), " unidades de area")

        print("El valor verdadero del area es: ", abs(integVerdadera(func, a, b)), " unidades de area")

        # calcular e imprimir el error relativo porcentual
        print("El error relativo porcentual verdadero es del: ", abs(((integVerdadera(func, a, b) - simpsonTresOctavos(func, a, b, n, 0, desicion)) / integVerdadera(func, a, b))) * 100, " %")

        print("El error absoluto es: ", abs(integVerdadera(func, a, b) - simpsonTresOctavos(func, a, b, n, 0, desicion)), " unidades de area")

else:
    if desicion == 2:        
        datosX = input("ingrese los puntos del eje X separados por un espacio entre c/u, al terminar de ingresar todo presione enter: \n")
        #se parsean los datos porque el input los ingresa como una cadena de caracteres
        arrays = datosX.split(" ")
        intervalos = []
        i = 0
        # convertir cada string a float y almacenarlos en un array para poder trabajar con ellos
        for i in range(len(arrays)):
            intervalos.append(float(arrays[i]))
        
        a = intervalos[0]
        b = intervalos[len(intervalos) - 1]

        print("\nEl valor del area por por combinacion de regla de Trapecio, Simposon 1/3 y  de Simpson 3/8 es: ", abs(intervalosDesiguales(func, intervalos)), " unidades de area")

        print("El valor verdadero del area es: ", abs(integVerdadera(func, a, b)), " unidades de area")

        # calcular e imprimir el error relativo porcentual
        print("El error relativo porcentual verdadero es del: ", abs(((integVerdadera(func, a, b) - intervalosDesiguales(func, intervalos)) / integVerdadera(func, a, b))) * 100, " %")

        print("El error absoluto es: ", abs(integVerdadera(func, a, b) - intervalosDesiguales(func, intervalos)), " unidades de area")

      
        
 
    
    

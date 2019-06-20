# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:22:07 2019

@author: Lolo Schleicher
"""


def coseno(x, n):
        import math
        
        #Convertir de grados Sexagesimales a radianes
        deSexaAradianes = (x * 6.283185307)/360
        
        
        #variable para ir acumulando las sumas de los terminos positivos de la serie infinita
        suma = 0
        
        #ciclo for que empieza con i=4(porque es el primer termino positivo de la serie, despues de la de orden 0 y 1), y va a recorrer hasta la cantidad de la aprox n que ingreso el usuario (utilizo n+1 porque sino me recorre hasta un numero menor a n, y yo necesito que sea menor o igual a n)
        #va en rangos de a 4 porque de esta manera va a poder calcular solo los terminos positivos
        for i in range(4, n+1, 4):
            
            #calculo del termino positivo de la serie
            cos = (math.pow(deSexaAradianes,i))/math.factorial(i)
            
            #Va acumulando las suma de los terminos positivos de la serie infinita
            suma += cos 
        
        
        #variable para ir acumulando las restas de los terminos negativos de la serie infinita
        resta = 0
        
        #ciclo for que empieza con i=2(porque es el primer termino negativo de la serie), y va a recorrer hasta la cantidad de la aprox n que ingreso el usuario (utilizo n+1 porque sino me recorre hasta un numero menor a n, y yo necesito que sea menor o igual a n)
        #va en rangos de a 4 porque de esta manera va a poder calcular solo los terminos negativos
        for i in range(2, n+1, 4):
            
            #calculo del termino negativo de la serie
            cos1 = -((math.pow(deSexaAradianes,i))/math.factorial(i))
        
            #Va acumulando las restas de los terminos negativos de la serie infinita
            resta += cos1 

        
        #El valor aproximado es el acumuador de los terminos positivos(suma) mas el acumulador de los terminos negativos(resta)
        #Ademas se suma el 1 que es el primer termino de la serie infinita
        valorAprox = 1 + (suma + resta)
        
        
        valorVerdadero = math.cos(deSexaAradianes)
        
        errorPorcentual = abs(((valorVerdadero - valorAprox)/valorVerdadero) * 100)
              
        print('\nEl valor aproximado es: ' + str(valorAprox))
        print("\nEl valor verdadero es: " + str(valorVerdadero))
        print("\nEl error porcentual es: " + str(errorPorcentual) + '%')
        
        
        
        

x = float(input('Ingresa el valor que desea calcular (en grados sexagesimales)'))
n = int(input('Ingresa el numero de orden'))
coseno(x, n)  
desicion = int(input("Si desea seguir aproximando el valor presione 1, de lo contario presione 2"))

while desicion == 1:
    n = int(input('Ingresa el numero de orden'))
    coseno(x, n)
    desicion = int(input("Si desea seguir aproximando el valor presione 1, sino cualquier otra tecla"))
    
print('chau')


        

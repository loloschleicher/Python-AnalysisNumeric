def funcion(n):
        import math
        
        #variable para ir acumulando las sumas de los terminos positivos de la serie infinita
        suma = 0
        
        #ciclo for que empieza con i=2(porque es el primer termino positivo de la serie, despues de la de orden 0 y 1), y va a recorrer hasta la cantidad de la aprox n que ingreso el usuario (utilizo n+1 porque sino me recorre hasta un numero menor a n, y yo necesito que sea menor o igual a n)
        #va en rangos de a 2 porque de esta manera va a poder calcular solo los terminos positivos
        for i in range(2, n+1, 2):
            
            #calculo del termino positivo de la serie
            e = (math.pow(5,i))/math.factorial(i)
            
            #Va acumulando las suma de los terminos positivos de la serie infinita
            suma += e
            
        #variable para ir acumulando las restas de los terminos negativos de la serie infinita
        resta = 0
        
        
        #ciclo for que empieza con i=1(porque es el primer termino negativo de la serie), y va a recorrer hasta la cantidad de la aprox n que ingreso el usuario (utilizo n+1 porque sino me recorre hasta un numero menor a n, y yo necesito que sea menor o igual a n)
        #va en rangos de a 4 porque de esta manera va a poder calcular solo los terminos negativos
        for i in range(1, n+1, 2):
            
            #calculo del termino negativo de la serie
            e1 = -((math.pow(5,i))/math.factorial(i))
            
            #Va acumulando las restas de los terminos negativos de la serie infinita
            resta += e1 

        
        #El valor aproximado es el acumuador de los terminos positivos(suma) mas el acumulador de los terminos negativos(resta)
        #Ademas se suma el 1 que es el primer termino de la serie infinita
        valorAprox = 1 + (suma + resta)
        
        
        valorVerdadero = 0.006737947
        errorVerdadero = valorVerdadero - valorAprox
        errorRelativo = abs(errorVerdadero / valorVerdadero * 100)
              
        print('\nEl valor aproximado para la funcion no inversa es: ' + str(valorAprox))
        print("\nEl valor verdadero para la funcion no inversa es: " + str(valorVerdadero))
        print("\nEl error porcentual para la funcion no inversa es: " + str(errorRelativo) + '%')


def funcionInversa(n):
        import math
             
        suma = 0
        
        
        for i in range(1, n+1, 1):
            e = ((math.pow(5,i))/math.factorial(i))       
            suma += e 

        valorAprox = 1 / suma
        
        
        valorVerdadero = 0.006737947
        errorVerdadero = valorVerdadero - valorAprox
        errorRelativo = abs(errorVerdadero / valorVerdadero * 100)
              
        print('\nEl valor aproximado para la funcion inversa es: ' + str(valorAprox))
        print("\nEl valor verdadero para la funcion inversa  es: " + str(valorVerdadero))
        print("\nEl error porcentual para la funcion inversa  es: " + str(errorRelativo) + '%')


        
n = int(input('Ingresa el numero de orden'))
funcion(n)  
funcionInversa(n)
desicion = int(input("Si desea seguir aproximando el valor presione 1, de lo contario presione 2"))

while desicion == 1:
    n = int(input('Ingresa el numero de orden'))
    funcion(n)
    funcionInversa(n)
    desicion = int(input("Si desea seguir aproximando el valor presione 1, sino cualquier otra tecla"))
    
print('chau')

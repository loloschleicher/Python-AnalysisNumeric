

   
def Es(numCifrasSig):
        import math

        #El valor que se usa para usar en la formula de tolerancia
        valorExp = 2 - numCifrasSig

        #Calcular la tolerancia
        Es = 0.5 * math.pow(10, valorExp)

        valorVerdadero = math.cos(0.3 * math.pi)

        #Calcular el error relativo porcentual
        Er = abs(((valorVerdadero - 1) / valorVerdadero) * 100)
    
        #Comparar el error con la tolerancia, con el primer termino de la serie
        if Er <= Es:
            
            print("El numero de terminos es: 1")


     
        iter = 2

        acum = 1

        x = 0.3 * math.pi
        
        aux = - 1
        
        #En caso de que el erro no sea menor o igual entonces empiezo calcular cada termino de la seria mientras el error sea mayor a la tolerancia
        while Er > Es:
            
            #variable auxiliar simplemente para alternar los signos de cada termino
            if aux == -1:

                valorAprox = - (math.pow(x, iter)/math.factorial(iter))

            else:
                valorAprox =  math.pow(x, iter)/math.factorial(iter)

            #vot acumulando los valores de cada termino de la serie
            acum += valorAprox
            
            #Calcular el error relativo porcentual
            Er = abs(((valorVerdadero - acum) / valorVerdadero) * 100)
            print(Er)
           
            iter += 2

            aux = aux * -1

            

        #Divido la cantidad de iteraciones sobre 2 porque la variable iter va saltando de 2 en 2, entonces al final en realidad la cantidad de iteraciones es la mitad de esa variable acumulada
        print("La cantidad de terminos es: " + str(iter/2))   
        print("\nEl valor verdadero es: " + str(valorVerdadero)) 
        print("\nEl valor aproximado en el termino " + str(iter/2) + ", es: " + str(acum))
        print("\nEl error relativo porcentual en el termino " + str(iter/2) + ", es: " + str(Er))
        print("\nEl valor de la tolerancia es: " + str(Es))



    

                


        
                
      
n = int(input('Ingresa la cantidad de cifras significativas'))
Es(n)


        

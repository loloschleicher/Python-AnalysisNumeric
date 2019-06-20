# -*- coding: utf-8 -*-
"""
Editor de Spyder

lolo Schleicher
"""

def resolvente(a, b, c):
    import math

    if a == 0:
        x = - (c/b)
        print("El valor de la raiz de la funcion lineal es: " + str(x))
    
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
            
           
            

print("Solucion de una funcion cuadratica")
a = float(input("Ingrese el valor de a: \n"))
b = float(input("Ingrese el valor de b: \n"))
c = float(input("Ingrese el valor de c: \n"))
resolvente(a, b, c) 
        
         
  
from colorama import init, Fore, Back, Style
from scipy.interpolate import lagrange
import json 
import math
import matplotlib.pyplot as plt
import numpy as np

#
#    Ejercicio 1
#

def funcionLinealizada(x):
    return ((-1/ (12000 * 0.00022)) * x + math.log(10))


def valoresCoeficientes(archivo):
    
    #Cargar datos desde json
    with open(archivo, "r") as datos:
        valores = json.load(datos)
    datos.close()

    #cantidad de valores
    n = len(valores)
    #sumatoria en x
    sumX = 0.0
    #sumatoria en y
    sumY = 0.0
    #sumatoria de x*y
    sumXY = 0.0
    #sumatoria de x^2
    sumX2 = 0.0

    valoresY = []

    # crear lista con valores x
    valoresX = []
    for x, y in valores.items():
        valoresX.append(float(x))
        valoresY.append(math.log(10 - float(y)))
        
    #calcular sumatorias
    for x in range(len(valoresX)):
        sumY = sumY + float(valoresY[x])
        sumX = sumX + float(valoresX[x])
        sumXY = sumXY + (float(valoresX[x]) * float(valoresY[x]))
        sumX2 = sumX2 + math.pow(float(valoresX[x]), 2)


    # calcular ajuste por minimos cuadrados
    a1 = ( (n* sumXY) - (sumX * sumY) ) / ((n * sumX2) - math.pow(sumX, 2) )
    a0 = ( sumY / n ) - ( a1 * ( sumX / n ) )

    return a0, a1

#
#EJERCICIO 2    
#

def graficaPreliminar(valoresX, valoresY):
    plt.plot(valoresX, valoresY, ".")
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.title("Grafica Preliminar de los datos Experimentales")
    plt.show()

def valorIncognita(archivo):
    a0, a1 = valoresCoeficientes(archivo)
    tauCalculado =( -1 /  a1)
    tauVerdadero = 12000*0.00022
    print("Valor del parametro incognita y calculo del error:\n" )
    print("Tau calculado: ", tauCalculado ,"s")
    print("Tau verdadero: ", tauVerdadero, "s")
    print("Error cometido:", tauVerdadero - tauCalculado)
    print("Error porcentual:", abs((((tauVerdadero - tauCalculado) / tauVerdadero) * 100)), " %")
    
#        
#EJERCICIO 3
#

def funcionExponencial(a0, a1, x):
    return ( math.exp(a0) * (1- math.exp(a1* x)))

def graficaSuperpuesta(valoresX, valoresY):    
    #almacenar lo que retorna la funcion valoresCoeficientes en la variable a0(el valor de a0) y en la variable a1 el valor de a1
    a0, a1 = valoresCoeficientes("datos.json")

    imagenesFuncion = []
    for x in valoresX:     
        imagenesFuncion.append(funcionExponencial(a0, a1, x))
    
    plt.plot(valoresX,imagenesFuncion, '-', label="Datos teoricos")
    
    plt.plot(valoresX, valoresY, ".", label="Datos experimentales")
    plt.title("Ajuste de Curva con ecuacion Exponencial")
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.legend()

    plt.show()





#EJERCICIO 4
def interpolacionLineal(valoresX, valoresY,x):
    #R = 12000
    #C = 0.00022
    #x = R * C
    xUno = 0.0
    xCero = 0.0
    fXcero = 0.0
    fXuno = 0.0
    posicion = 0
       
    for i in range(len(valoresX)):
        #Con este if estoy guardando en la variable xCero el valor anterior mas proximo al tau, y en la variable xUno el valor siguiente mas proximo a tau y guardo la posicion del xCero
        if valoresX[i] < x:
            xCero = valoresX[i]
            posicion = i
            xUno = valoresX[i+1]
               
    for y in range(len(valoresY)) :
        # Con este if comparo cuando la posicion de y es = a la posicion de xCero, entonces guardo el valor de esa posicion(seria mi fXcero) y el alor del siguiente (fXuno)
        if posicion == y:
            fXcero = valoresY[y]
            fXuno = valoresY[y+1]
    #formula de interpolacion lineal de Newton        
    fX = fXcero + (((fXuno - fXcero) / (xUno - xCero)) * (x - xCero))
    print("El valor es: ",fX, "V (volts) para un tau de", x)





#EJERCICIO 5
def ajusteSinCuadradoMin(valoresX, valoresY):
    #Chebyshev ajusta una curva a traves de un polinomio, en esta funcion  le estoy pasando los datos experimentales y el grado del polinomio que quiero ajustar 
    p = np.polynomial.Chebyshev.fit(valoresX, valoresY, 90)    
    plt.plot(valoresX, valoresY, 'r.', label="Datos Experimentales")
    t = np.linspace(0, 10, 10)
    plt.plot(t, p(t), '-', lw=2, label="Curva adaptada")
    plt.title("Ajuste de Curva con Chebyshev") 
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.show()

if __name__ == "__main__":

        
    # Cargar datos desde json
    with open("datos.json", "r") as datos:
        valores = json.load(datos)
    datos.close()

    #convertir dict a list
    valoresX = []
    valoresY = []

    #convertir string a float
    for x, y in valores.items():
        valoresX.append(float(x))
        valoresY.append(float(y))

    
    R = 12000
    C = 0.00022
    x = R * C
    #EJERCICIO 1
    print(f"\n\n{Fore.RED}Ejercicio1:{Style.RESET_ALL} \nLos valores de los coeficientes a0 y a1 son: " + str(valoresCoeficientes("datos.json")) + " Respectivamente" )

    #EJERCICIO 2
    print(f"\n \n{Fore.RED}Ejercicio2:{Style.RESET_ALL}")
    graficaPreliminar(valoresX, valoresY)
    valorIncognita("datos.json")

    #EJERCICIO 3
    print(f"\n\n{Fore.RED}Ejercicio 3:{Style.RESET_ALL} \nGrafica superpuesta De Los Datos Experimentales y de los valores Obtenidos por la ecuacion linealizada")
    graficaSuperpuesta( valoresX, valoresY)

    #EJERCICIO 4
    print(f"\n\n{Fore.RED}Ejercicio 4:{Style.RESET_ALL}\nInterpolacion lineal de Newton")
    interpolacionLineal(valoresX, valoresY,x)

    #EJERCICIO 5
    print(f"\n\n{Fore.RED}Ejercicio 5:{Style.RESET_ALL} \nAjuste de curva con Chebyshev:")
    ajusteSinCuadradoMin(valoresX, valoresY)
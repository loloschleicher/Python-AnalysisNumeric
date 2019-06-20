import numpy as np
import math

a = np.array([[0, 2, 5],
               [2, 1, 1],
               [3, 1, 0]])

b = np.array([9, 9, 10])
x = np.linalg.solve(a, b)
#la funcion det() recibe una matriz cualquiera y devuelve su determinante 
determinante = np.linalg.det(a)
print("Los valores de x1, x2, x3 son: " + str(x) + " respectivamente")
print("El valor del determinante es: " + str(determinante))
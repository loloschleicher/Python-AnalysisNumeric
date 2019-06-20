import numpy as np

#declaracion de matrices
a = np.matrix([[4, 7], [1, 2], [5, 6]])
b = np.matrix([[4, 3, 7], [1, 2, 7], [1, 0, 4]])
c = np.matrix([[3], [6], [1]])
d = np.matrix([[9, 4, 3, -6], [2, -1, 7, 5]])
e = np.matrix([[1, 5, 8], [7, 2, 3], [4, 0, 6]])
f = np.matrix([[3, 0, 1], [1, 7, 3]])
g = np.matrix([[7, 6, 4]])
identidad = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

punto1 = print("Punto 1 \n" + str(e + b)) 
#punto2 =  no se puede sumar porque no son de las mismas dimensiones
punto3 = print("Punto 3 \n" + str(b - e))
punto4 = print("Punto 4 \n" + str(7 * b))
punto5 = print("Punto 5 \n" + str(e * b))
punto6 = print("Punto 6 \n" + str(np.transpose(c))) #transpose es una funcion de numpy que recibe como parametro una matriz y devuelve su traspuesta
punto7 = print("Punto 7 \n" + str(b * a))
punto8 = print("Punto 8 \n" + str(np.transpose(d)))
#punto9 = no se puede resolver porque la cantidad de columnas de a no es igual a la cantidad de filas de c
punto10 = print("Punto 10 \n" + str(identidad * b))
punto11 = print("Punto 11 \n" + str(np.transpose(e) * e))
punto12 = print("Punto 12 \n" + str(np.transpose(c) * c))
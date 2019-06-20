import json

#cargar datos desde archivos
with open("datos_carga_t_Vc.dat", "r") as archivo:
    data = archivo.read()
archivo.close()

# Separar datos en x e y
# los valores en x estan delimitados por un caracter \n al final
x = data[3:data.index("\n")]
y = data[data.index("\n")+4:len(data)-1]

# Partir string en valores discretos
y = y.split("   ")
x = x.split("   ")

# Formar diccionario con los valores en x como llaves
valores = dict(zip(x, y))

# Crear json con diccionario
with open("datos.json", "w") as archivo_salida:
    json.dump(valores, archivo_salida, indent=4)
archivo_salida.close()



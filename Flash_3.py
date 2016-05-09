from datetime import datetime
import sys
import math
import numpy as np

entrada = sys.argv[1]
salida = sys.argv[2]
tamano = int(sys.argv[3])

# Interpreta elemento a elemento (entendiendo como tal a lo que está comprendido entre ',') 
# cada línea del archivo .csv que se le pasa como parámetro.
# Convierte los timestamps al formato IS-8601, los numeros a float y mantiene los 'NA' como strings.
# Genera una lista de listas en donde cada elemento corresponde a la interpretación de una línea. 
def interpretar(csv):
    res = []
    for i in csv.readlines():
        linea = i.split(',')
        linea[0] = datetime.strptime(linea[0], '%Y-%m-%dT%H:%M:%S')
        for j in range(1, len(linea)):
            if linea[j] == 'NA' or linea[j] == 'NA\n':
                pass
            else:
                linea[j] = float(linea[j])
        res.append(linea)
    return res

# Devuelve el promedio de los elementos de la secuencia recibida con 2 cifras decimales.
# Si alguno de estos es NA, el resultado también lo es.
def promedio(lista):
    res = 'NA'
    i = 0
    suma = 0
    while i < len(lista) and not(lista[i] == 'NA' or lista[i] == 'NA\n'):
        suma += lista[i]
        i += 1
    if i == len(lista):
        res = round(suma / i, 2)
    return res

# Genera un rango de un tamaño fijo (parámetro) que recorre una lista hasta llegar al último
# elemento.
# Si la lista contiene timestamps, calcula la diferencia en segundos entre el extremo "superior" y
# el "inferior". En el caso contrario, calcula el promedio de todos los elementos.
# Si el tamaño de la ventana supera la longitud de la lista o es 0, la función retorna [].
def ventanaDeslizante(lista, tamano):
    res = []
    cota_inf = 0
    cota_sup = tamano-1
    while cota_sup < len(lista):
        if type(lista[cota_inf]) == float or type(lista[cota_inf]) == str:
            c = promedio(lista[cota_inf:cota_sup+1])
        else:
            c = (lista[cota_sup] - lista[cota_inf]).total_seconds()
        res.append(c)
        cota_inf += 1
        cota_sup += 1
    return res        

# Devuelve el resultado de aplicar ventanaDeslizante a cada columna del arreglo que recibe
# como parámetro.
def analizarPorColumnas(arreglo, tamano):
    res = []
    # arreglo.shape[1] = número de columnas.
    for i in range(0, arreglo.shape[1]):
        # Selecciona la columna i.
        columna = arreglo[:, i]
        columna = ventanaDeslizante(columna, tamano)
        res.append(columna)
    # Agrega cada columna de arreglo como fila de res.
    res = np.array(res)
    # Intercambia filas por columnas.
    res = np.transpose(res)
    return res

def main(entrada, salida, tamano):
    f = open(entrada, 'r')
    archivo_interpretado = interpretar(f)
    f.close()
    # Si el archivo de entrada posee una sola linea (o ninguna), el de salida será igual.
    if len(archivo_interpretado) > 1:
        archivo_interpretado = np.array(archivo_interpretado)
        res = analizarPorColumnas(archivo_interpretado, tamano)
    else:
        res = np.array(archivo_interpretado)
    g = open(salida, 'w')
    # res.shape[0] corresponde al número de filas de res.
    for i in range(res.shape[0]):
        # Escribe en el archivo de salida los elementos de i como str separados por ','.
        g.write(','.join(map(str, res[i])) + '\n')
    g.close()

print(main(entrada, salida, tamano))
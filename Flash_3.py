from datetime import datetime
import sys
import math
import numpy as np

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

def main(entrada, salida, tamano):
    f = open(entrada, 'r')
    archivo_interpretado = interpretar(f)
    f.close()
    if len(archivo_interpretado) > 1:
        archivo_interpretado = np.array(archivo_interpretado)
        res = magia(archivo_interpretado, tamano)
    else:
        res = np.array(archivo_interpretado)
    g = open(salida, 'w')
    for i in range(res.shape[0]):
        g.write(','.join(map(str, res[i])) + '\n')
    g.close()
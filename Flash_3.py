from datetime import datetime
import sys
import math
import numpy as np

entrada = sys.argv[1]
salida = sys.argv[2]
tamano = int(sys.argv[3])

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

def magia(arreglo, tamano):
    res = []
    for i in range(0, arreglo.shape[1]):
        col = arreglo[:, i]
        col = ventanaDeslizante(col, tamano)
        res.append(col)
    res = np.array(res)
    res = np.transpose(res)
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

print(main(entrada, salida, tamano))
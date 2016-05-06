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
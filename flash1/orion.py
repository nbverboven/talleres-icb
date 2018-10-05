from math import sqrt

##
# La función devuelve True si x solamente posee 2 divisores:
# 1 y él mismo.
##
def esPrimo(x):
    cant_divisores = 0
    # Chequeo que no existan divisores de x en el rango 
    # [2, sqrt(x)] (alcanza con ver hasta la raíz cuadrada
    # de x)
    for posible_divisor in range(2, int(sqrt(x))+1):
        if x%posible_divisor == 0:
            cant_divisores += 1
    return cant_divisores == 0

##
# Devuelve en x-ésimo primo de Mersenne.
##
def Orion(x):
    cant_encontrados = 0
    j = 0
    # Se inicializa esta variable con 2 puesto que es el primer caso de interés.
    # (2**2) - 1 = 3, que resulta el primer primo de la forma (2**n) - 1.
    potencia = 2
    while cant_encontrados < x:
        j = (2**potencia) - 1
        if esPrimo(j):
            cant_encontrados += 1
        potencia += 1
    return j

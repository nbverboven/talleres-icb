#La función devuelve True si x solamente posee 2 divisores:
#1 y él mismo.
def esPrimo(x):
    contador = 0
    for posible_divisor in range(1, x+1):
        if x%posible_divisor == 0:
#El contador almacena el número de divisores de x.
            contador += 1
    return contador == 2

#Devuelve en x-ésimo primo de Mersenne.
def Orion(x):
    i = 0
    j = 0
#Se inicializa esta variable con 2 puesto que es el primer caso de interés.
#(2**2) - 1 = 3, que resulta el primer primo de la forma (2**n) - 1.
    potencia = 2
    while i < x:
        j = (2**potencia) - 1
        if esPrimo(j):
#Este contador aumenta con cada primo de Mersenne hallado.
            i += 1
        potencia += 1
    return j
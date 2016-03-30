def esPrimo(x):
    contador = 0
    for posible_divisor in range(1, x+1):
        if x%posible_divisor == 0:
            contador += 1
    return contador == 2

def Orion(x):
    i = 0
    j = 0
    potencia = 2
    while i < x:
        j = (2**potencia) - 1
        if esPrimo(j):
            i += 1
        potencia += 1
    return j
def Cavenaghi(x):
#Defino el valor inicial de a como 0.
#Si el parámetro recibido por la función fuera negativo, el rango del iterador es vacío
#y la sumatoria será 0.
    a = 0
    for i in range(1, x+1):
        a += ((2 * ((-1)**(i + 1))) / (2*i - 1))
    return a
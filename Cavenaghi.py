def Cavenaghi(x):
    a = 0
    for i in range(1, x+1):
        a += ((2 * ((-1)**(i + 1))) / (2*i - 1))
    return a
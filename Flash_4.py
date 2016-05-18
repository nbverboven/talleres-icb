import numpy as np

def NReinas(n):
	tablero = np.array([[False for i in range(n)] for j in range(n)])
	resolver(tablero, n, 0)
	print(tablero)
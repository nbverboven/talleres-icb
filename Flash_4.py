import numpy as np

def noAmenazada(tablero, pos_fila, pos_columna):
	return tablero[pos_fila, :].sum() == 1 and tablero[:, pos_columna].sum() == 1 and diagonalesOk(tablero, pos_fila, pos_columna)

def NReinas(n):
	tablero = np.array([[False for i in range(n)] for j in range(n)])
	resolver(tablero, n, 0)
	print(tablero)
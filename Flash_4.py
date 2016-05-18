import numpy as np

asd = np.array([[False, False,  True, False],
 			  [ True, False, False, False],
 			  [False, False, False,  True],
 			  [False,  True, False, False]])

def diagonalesOk(tablero, pos_fila, pos_columna):
	return np.diag(tablero, pos_columna-pos_fila).sum() == 1 and np.diag(tablero.transpose(), pos_fila).sum() == 1
	# i = 0
	# flag = True
	# while i < tablero.shape[0] and flag:
	# 	j = 0
	# 	while j < tablero.shape[1] and flag:
	# 		if abs(pos_fila - i) == abs(pos_columna - j) and not (pos_fila == i) and not( pos_columna == j) and tablero[i, j]:
	# 			flag = False
	# 		j += 1
	# 	i += 1
	# return flag

def noAmenazada(tablero, pos_fila, pos_columna):
	return tablero[pos_fila, :].sum() == 1 and tablero[:, pos_columna].sum() == 1 and diagonalesOk(tablero, pos_fila, pos_columna)

def NReinas(n):
	tablero = np.array([[False for i in range(n)] for j in range(n)])
	resolver(tablero, n, 0)
	print(tablero)
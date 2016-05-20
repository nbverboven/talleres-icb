
asd1 = [[False, False,  True, False],
 		[ True, False, False, False],
 		[False, False, False,  True],
 		[False,  True, False, False]]

asd2 = [[True, False,  True, False],
 		[ True, False, False, False],
 		[False, False, False,  True],
 		[False,  True, False, False]]


def filaOk(lista):
	reinas_en_fila = lista.count(True)
	return reinas_en_fila == 1

def columnaOk(tablero, pos_columna):
	reinas_en_columna = 0
	for fila in tablero:
		if fila[pos_columna]:
			reinas_en_columna += 1
	return reinas_en_columna == 1

def diagonalesOk(tablero, pos_fila, pos_columna):
	diagonales = []
	for fila in range(len(tablero)):
		for columna in range(len(tablero)):
			if abs(pos_fila - fila) == abs(pos_columna - columna):
				diagonales.append(tablero[fila][columna])
	return diagonales.count(True) == 1

def noAmenazada(tablero, pos_fila, pos_columna):
	return filaOk(tablero[pos_fila]) and columnaOk(tablero, pos_columna) and diagonalesOk(tablero, pos_fila, pos_columna)

def resolver(tablero, numero_reinas, fila):
	if numero_reinas == 0:
		return True
	else:
		for columna in range(len(tablero)):
			tablero[fila][columna] = True
			if not(noAmenazada(tablero, fila, columna) and resolver(tablero, numero_reinas-1, fila+1)):
				tablero[fila][columna] = False
			else:
				return True

def NReinas(n):
	tablero = [[False for fila in range(n)] for j in range(n)]
	resolver(tablero, n, 0)
	for i in tablero:
		print(str(i) + '\n')
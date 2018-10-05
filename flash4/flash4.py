# Verifica que haya una sola reina en la fila que recibe como parametro.
def filaOk(lista):
	reinas_en_fila = lista.count(True)
	return reinas_en_fila == 1

# Verifica que haya una sola reina en la columna pos_columna.
def columnaOk(tablero, pos_columna):
	reinas_en_columna = 0
	fila = 0
	while fila < len(tablero) and reinas_en_columna < 2:
		if tablero[fila][pos_columna]:
			reinas_en_columna += 1
		fila += 1
	return reinas_en_columna == 1

# Verifica que haya una sola reina en las diagonales que atraviesan la 
# posicion tablero[pos_fila][pos_columna].
def diagonalesOk(tablero, pos_fila, pos_columna):
	diagonales = []
	for fila in range(len(tablero)):
		for columna in range(len(tablero)):
			if abs(pos_fila - fila) == abs(pos_columna - columna):
				diagonales.append(tablero[fila][columna])
	return diagonales.count(True) == 1

# Devuelve True si, para una dada reina en una posicion 
# tablero[pos_fila][pos_columna], esta es la unica en su fila, su columna y 
# en las dos diagonales que contienen su ubicacion.
def reinaNoAmenazada(tablero, pos_fila, pos_columna):
	return filaOk(tablero[pos_fila]) and columnaOk(tablero, pos_columna) and diagonalesOk(tablero, pos_fila, pos_columna)

# Resuelve el tablero utilizando el metodo de backtracking.
# Una consideracion que se tuvo con el fin de reducir el tiempo de ejecucion 
# (aunque no en el peor caso) fue que, si se logra ubicar a una reina en una 
# posicion, la funcion no sigue probando con las columnas restantes sino 
# que prosigue a la siguiente fila. 
def resolver(tablero, numero_reinas, fila):
	if numero_reinas == 0:
		return True
	else:
		for columna in range(len(tablero)):
			tablero[fila][columna] = True
			if not(reinaNoAmenazada(tablero, fila, columna) and resolver(tablero, numero_reinas-1, fila+1)):
				tablero[fila][columna] = False
			else:
				return True

def NReinas(n):
	# Genera un tablero de n*n.
	tablero = [[False for fila in range(n)] for j in range(n)]
	resolver(tablero, n, 0)
	for i in tablero:
		print(str(i) + '\n')
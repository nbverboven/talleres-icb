def estaEn(elemento, lista):
	flag = False
	for i in lista:
		if i == elemento:
			flag = True
	return flag

def cantAparicionesSub(lista1, lista2):
	contador = 0
	for i in lista1:
		if estaEn(i, lista2):
			contador += 1
	return contador

#####################################################

def decreceHastaElFinal(lista):
	a = 0
	while a < len(lista)-1 and lista[a] > lista[a+1]:
		a += 1
	return len(lista) >= 2 and a == len(lista)-1

def listaTriangular(lista):
	flag = False
	indice_actual = 0
	while  indice_actual < len(lista)-1 and lista[indice_actual] < lista[indice_actual+1]:
		if decreceHastaElFinal(lista[indice_actual+1:]):
			flag = True
		indice_actual += 1
	return flag

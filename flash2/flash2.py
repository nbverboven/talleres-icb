##
# Verifica que un elemento se encuentre en una lista.
##
def estaEn(elemento, lista):
	flag = False
    i = 0
    while i < len(lista) and flag == False:
		if i == elemento:
			flag = True
        i += 1
	return flag

##
# Cuenta la cantida de elementos de la lista1 presentes en la lista2.
##
def cantAparicionesSub(lista1, lista2):
	contador = 0
	for i in lista1:
		if estaEn(i, lista2):
			contador += 1
	return contador

##
# Verifica si los elementos de una lista, de longitud 2 o mayor, se
# encuentran ordenados de forma estrictamente decreciente.
##
def decreceHastaElFinal(lista):
	a = 0
	while a < len(lista)-1 and lista[a] > lista[a+1]:
		a += 1
	return len(lista) >= 2 and a == len(lista)-1

##
# Verifica si la lista pasada como parametro es triangular.
# Listas del estilo [1, 2, 3, 2, 1] , [1, 2, 3, 2], [1, 3, 2, 1] son triangulares.
# La lista vacía, las de longitud menor a 3 o aquellas de la forma [1, 2, 2, 1] 
# no se consideran triangulares.
##
def listaTriangular(lista):
	flag = False
	indice_actual = 0
	while  indice_actual < len(lista)-1 and lista[indice_actual] < lista[indice_actual+1] and flag == False:
		if decreceHastaElFinal(lista[indice_actual+1:]):
			flag = True
		indice_actual += 1
	return flag

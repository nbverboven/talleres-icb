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

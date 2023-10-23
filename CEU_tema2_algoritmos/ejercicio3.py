def magia_numerica(lista):
    listaUnica = list(set(lista))
    listaOrdenada = sorted(listaUnica, reverse = True)

    listaPares = []
    for i in listaOrdenada:
        if (i%2 == 0):
            listaPares.append(i)
    
    suma = 0

    for i in listaPares:
        suma += i
    
    listaPares.insert(0, suma)

    print(listaPares)



lista = [1, 1, 3, 6, 2, 9, 61, 75, 13, 8, 7, 7]

magia_numerica(lista)

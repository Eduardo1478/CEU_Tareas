import random
import numpy as np

#Metodo de Gauss
def iterativo(matriz):
    n = len(matriz)
    det = 1
    for i in range(n):

        max_index = max(range(i, n), key=lambda x: abs(matriz[x][i]))
        if i != max_index:
            matriz[i], matriz[max_index] = matriz[max_index], matriz[i]
            det *= -1

        if matriz[i][i] == 0:
            return 0

        det *= matriz[i][i]

        for j in range(i + 1, n):
            factor = matriz[j][i] / matriz[i][i]
            for k in range(i, n):
                matriz[j][k] -= factor * matriz[i][k]

    return round(det, 1)

def recursivo(matriz):
    n = len(matriz)

    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for i in range(n):
            submatrix = [row[:i] + row[i+1:] for row in matriz[1:]]
            det += matriz[0][i] * recursivo(submatrix) * (-1)**i
        return round(det, 1)


rows = 3
columns = 3

#Se llena la matriz automaticamente
matriz = [[random.randint(1, 10) for _ in range(columns)] for _ in range(rows)]

print("matriz: " + str(matriz))

print("determinante del iterativo: " + str(iterativo(matriz)))
print("determinante del recursivo: " + str(recursivo(matriz)))
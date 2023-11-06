import random
import numpy as np

def iterativo(matriz):
    determinante = np.linalg.det(matriz)
    determinante_redondeado = round(determinante, 1)    

    return(determinante_redondeado)

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
        return det


rows = 3
columns = 3

matriz = [[random.randint(1, 10) for _ in range(columns)] for _ in range(rows)]

print("matriz: " + str(matriz))

print("determinante del iterativo: " + str(iterativo(matriz)))
print("determinante del recursivo: " + str(recursivo(matriz)))
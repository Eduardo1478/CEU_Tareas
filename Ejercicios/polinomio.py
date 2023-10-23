def recursividad(pol, x):
    if len(pol) == 0:
        return 0
    else:
        return x*recursividad(pol[:-1], x) + pol[-1]


polinomio = [5, -2, 3, -2]
x = 2

print(recursividad(polinomio, x))
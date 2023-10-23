def recursividad(n1, n2):
    if n2 == 0:
        return n1

    n3 = n1 - n2
    return recursividad(n2, n3)
    
    

nuemro1 = 120

numero2 = 75

print(recursividad(nuemro1, numero2))



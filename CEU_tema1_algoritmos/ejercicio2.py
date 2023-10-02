import math

capital_inicial = 1000

interes = float(input("Introduce tasa de interes"))

interes = 1 + (interes / 100)

tiempo = int(input("Por cuantos años"))

resultado = 1000*(interes ** tiempo)

print("El resultado es " + str(resultado))


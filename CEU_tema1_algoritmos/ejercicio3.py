lista1 = ["casa", "perro", "laptop", "telefono", "manzana", "cabeza", "silla", "aire", "fuego"]
lista2 = ["laptop", "abanico", "mesa", "alfombra", "enchufe", "ventana", "telefono", "silla", "piso", "aire"]

lista3 = []

print("Hello")

for i in lista1:
    for ii in lista2:
        if i == ii:
            lista3.append(i)

print(lista3)
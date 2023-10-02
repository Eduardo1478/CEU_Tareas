personajes = [("Tomas", 1),
              ("Alberto", 1),
              ("Ardilla", 0),
              ("Robot", 0),
              ("Maria", 1),
              ("Perro", 0),
              ("Dragon", 0),
              ("Zombie", 0),
              ("Fernanda", 1),
              ("Cristobal", 1)]

lista_humanos = []
lista_no_humanos = []

for element in personajes:
    if(element[1] == 1):
        lista_humanos.append(element)
    if(element[1] == 0):
        lista_no_humanos.append(element)

humanos_sort = sorted(lista_humanos, key=lambda x: x[0])
no_humanos_sort = sorted(lista_no_humanos, key=lambda x: x[0])


print("Humanos: ")

for item in humanos_sort:
    print(item[0])

print("\n")

print("No Humanos: ")

for item in no_humanos_sort:
    print(item[0])



naves_espaciales = [
    {
        "nombre": "Iberia",
        "longitud": 50,
        "tripulantes": 10,
        "pasajeros": 20
    },
    {
        "nombre": "RyanAir",
        "longitud": 40,
        "tripulantes": 8,
        "pasajeros": 15
    },
    {
        "nombre": "Cometa Veloz",
        "longitud": 60,
        "tripulantes": 12,
        "pasajeros": 25
    },
     {
        "nombre": "Delta",
        "longitud": 60,
        "tripulantes": 12,
        "pasajeros": 127
    },
     {
        "nombre": "Titán del Cosmos",
        "longitud": 60,
        "tripulantes": 10,
        "pasajeros": 47
    },
     {
        "nombre": "GX Luftansa",
        "longitud": 60,
        "tripulantes": 232,
        "pasajeros": 5
    }
]

naves_ordenadas_por_nombre = sorted(naves_espaciales, key=lambda x: x["nombre"])
print("Naves ordenadas por nombre: ")
for nave in naves_ordenadas_por_nombre:
    print(nave["nombre"])
print("\n")


naves_ordenadas_por_longitud = sorted(naves_espaciales, key=lambda x: x["longitud"])
print("Naves ordenadas por longitud: ")
for nave in naves_ordenadas_por_nombre:
    print(nave["nombre"])
print("\n")


print("Informacion del cometa veloz: ")
print(naves_espaciales[2])
print("\n")


print("Titán del Cosmos: ")
print(naves_espaciales[4])
print("\n")


naves_ordenadas_por_pasajeros = sorted(naves_espaciales, key=lambda x: x["pasajeros"], reverse=True)
print("Top 5 naves en pasajeros: ")
for nave in naves_ordenadas_por_pasajeros[:5]:
    print(nave["nombre"])
print("\n")


naves_ordenadas_por_tripulantes = sorted(naves_espaciales, key=lambda x: x["tripulantes"], reverse=True)
print("Nave con mas tripulantes: ")
for nave in naves_ordenadas_por_tripulantes[:1]:
    print(nave["nombre"])
print("\n")

print("Naves que empiezan con GX: ")
for nave in naves_espaciales:
    if nave["nombre"].startswith("GX"):
        print(nave)
def agregar_item(inventario, item):
    for elemento in inventario:
        if(item == elemento):
            print("Error de tipo ValueError, el elemento ya existe en el inventario")
            return False

    inventario.append(item)
    print("Inventario Actual: " + str(inventario))    
    return True        


inventario = ["Espada", "Escudo", "Elixir", "Arco", "Bombas", "Armadura", "Posion", "Casco"]

while True:
    item_nuevo = str(input("\n" + "Escribe un nuevo Item o 'Fin' para finalizar: "))
    if(item_nuevo == "Fin"):
        break
    agregar_item(inventario, item_nuevo)







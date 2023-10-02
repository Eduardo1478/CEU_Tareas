misiones = [("Mision Alpha", 2), ("Mision Bravo", 1), ("Mision Charlie", 4), ("Mision Delta", 3), ("Tutorial", 0), ("Mision Final", 5), ("Mision Echo", 2), ("Mision Foxtrot", 3)]

misiones_sort = sorted(misiones, key=lambda x: x[1])

for item in misiones_sort:
    print(item[0])
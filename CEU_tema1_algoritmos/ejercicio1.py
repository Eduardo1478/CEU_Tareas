datos = "002 atsap"
datos_mirror = datos[::-1]

words = datos_mirror.split()

receta = words[0]
calorias = words[1]

print("La receta de " + receta + " contiene " + calorias + " calorías")
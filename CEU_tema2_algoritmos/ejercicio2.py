texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

textoFormat = texto.split('#')

print(textoFormat[0].capitalize() + "...")

for i in textoFormat[1:]:
    print("\t" + "•" + i.capitalize() + ".")







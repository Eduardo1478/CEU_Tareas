class Pokemon:
    def __init__(self, nombre, numero, tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad

class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if nodo is None:
            return NodoArbol(clave, valor)

        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar(nodo.derecha, clave, valor)

        return nodo

    def buscar(self, clave):
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        if nodo is None or nodo.clave == clave:
            return nodo.valor

        if clave < nodo.clave:
            return self._buscar(nodo.izquierda, clave)
        else:
            return self._buscar(nodo.derecha, clave)

# Crear instancias de ArbolBinario para cada índice
indice_nombre = ArbolBinario()
indice_numero = ArbolBinario()
indice_tipo = ArbolBinario()

# Datos de muestra de Pokémon
datos_pokemon = [
    Pokemon("Bulbasaur", 1, "Planta/Veneno", "Psíquico"),
    Pokemon("Ivysaur", 2, "Planta/Veneno", "Psíquico"),
    Pokemon("Venusaur", 3, "Planta/Veneno", "Psíquico"),
    Pokemon("Charmander", 4, "Fuego", "Agua"),
    Pokemon("Charmeleon", 5, "Fuego", "Agua"),
    Pokemon("Charizard", 6, "Fuego/Volador", "Agua"),
    Pokemon("Squirtle", 7, "Agua", "Planta"),
    Pokemon("Wartortle", 8, "Agua", "Planta"),
    Pokemon("Blastoise", 9, "Agua", "Planta"),
    Pokemon("Pikachu", 25, "Eléctrico", "Tierra"),
    Pokemon("Raichu", 26, "Eléctrico", "Tierra"),
    Pokemon("Jigglypuff", 39, "Normal/Hada", "Acero"),
    Pokemon("Wigglytuff", 40, "Normal/Hada", "Acero"),
    Pokemon("Psyduck", 54, "Agua", "Planta"),
    Pokemon("Golduck", 55, "Agua", "Planta"),
    Pokemon("Machop", 66, "Lucha", "Psíquico"),
    Pokemon("Machoke", 67, "Lucha", "Psíquico"),
    Pokemon("Machamp", 68, "Lucha", "Psíquico"),
    Pokemon("Gyarados", 130, "Agua/Volador", "Eléctrico"),
    Pokemon("Vaporeon", 134, "Agua", "Planta"),
    Pokemon("Jolteon", 135, "Eléctrico", "Tierra"),
    Pokemon("Flareon", 136, "Fuego", "Agua"),
    Pokemon("Snorlax", 143, "Normal", "Lucha"),
    Pokemon("Dragonite", 149, "Dragón/Volador", "Hielo"),
    Pokemon("Mewtwo", 150, "Psíquico", "Siniestro"),
    Pokemon("Mew", 151, "Psíquico", "Siniestro"),
    Pokemon("Tyranitar", 248, "Roca/Siniestro", "Lucha"),
    Pokemon("Blaziken", 257, "Fuego/Lucha", "Agua"),
    Pokemon("Gardevoir", 282, "Psíquico/Hada", "Acero"),
]

# Llenar los árboles binarios con los datos de Pokémon
for pokemon in datos_pokemon:
    indice_nombre.insertar(pokemon.nombre, pokemon)
    indice_numero.insertar(pokemon.numero, pokemon)
    indice_tipo.insertar(pokemon.tipo, pokemon)

# Ejemplo de uso: Buscar un Pokémon por nombre
nombre_pokemon_a_buscar = "Charmander"
pokemon_encontrado = indice_nombre.buscar(nombre_pokemon_a_buscar)

if pokemon_encontrado:
    print(f"Pokemon encontrado: {pokemon_encontrado.nombre}, Número: {pokemon_encontrado.numero}, Tipo: {pokemon_encontrado.tipo}, Debilidad: {pokemon_encontrado.debilidad}")
else:
    print(f"Pokemon con el nombre '{nombre_pokemon_a_buscar}' no encontrado.")

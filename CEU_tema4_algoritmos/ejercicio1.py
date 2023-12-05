import heapq
from collections import defaultdict

class NodoHuffman:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(tabla_frecuencias):
    heap = [NodoHuffman(simbolo, frecuencia) for simbolo, frecuencia in tabla_frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)

        nuevo_nodo = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        nuevo_nodo.izquierda = izquierda
        nuevo_nodo.derecha = derecha

        heapq.heappush(heap, nuevo_nodo)

    return heap[0]

def generar_codigos_huffman(raiz, codigo_actual="", diccionario_codigos=None):
    if diccionario_codigos is None:
        diccionario_codigos = {}

    if raiz.simbolo is not None:
        diccionario_codigos[raiz.simbolo] = codigo_actual
    if raiz.izquierda is not None:
        generar_codigos_huffman(raiz.izquierda, codigo_actual + "0", diccionario_codigos)
    if raiz.derecha is not None:
        generar_codigos_huffman(raiz.derecha, codigo_actual + "1", diccionario_codigos)

    return diccionario_codigos

def decodificar_mensaje(mensaje_codificado, diccionario_codigos):
    mensaje_decodificado = ""
    codigo_actual = ""
    
    for bit in mensaje_codificado:
        codigo_actual += bit
        for simbolo, codigo in diccionario_codigos.items():
            if codigo_actual == codigo:
                mensaje_decodificado += str(simbolo + " ")
                codigo_actual = ""
                break

    return mensaje_decodificado


tabla_frecuencias = {
    'Sphinx': 5,
    'Pyramid': 7,
    'Lotus': 8,
    'Scarab': 9,
    'Obelisk': 10,
    'Djed': 11,
    'Eye of Horus': 12,
    'Ankh': 15
}

raiz_arbol = construir_arbol_huffman(tabla_frecuencias)

diccionario_codigos = generar_codigos_huffman(raiz_arbol)

print("\nCódigos Huffman:")
for simbolo, codigo in diccionario_codigos.items():
    print(f"{simbolo}: {codigo}")

mensaje_1_codificado = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100."

mensaje_2_codificado = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"

mensaje_1_decodificado = decodificar_mensaje(mensaje_1_codificado, diccionario_codigos)
mensaje_2_decodificado = decodificar_mensaje(mensaje_2_codificado, diccionario_codigos)


print("\nMensaje 1 decodificado:")
print(mensaje_1_decodificado)

print("\nMensaje 2 decodificado:")
print(mensaje_2_decodificado)

espacio_original = len(mensaje_1_decodificado + mensaje_2_decodificado)
espacio_comprimido = len(mensaje_1_codificado + mensaje_2_codificado)

print("\nEspacio de memoria necesario:")
print(f"Original: {espacio_original} bits")
print(f"Comprimido: {espacio_comprimido} bits")
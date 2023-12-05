import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, origen, destino, peso):
        self.vertices[origen][destino] = peso
        self.vertices[destino][origen] = peso

def dijkstra(grafo, inicio, fin):
    cola_prioridad = [(0, inicio)]
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0

    while cola_prioridad:
        distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[vertice_actual]:
            continue

        for vecino, peso in grafo.vertices[vertice_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias[fin]



grafo_tierra_media = Grafo()

grafo_tierra_media.agregar_vertice("Rivendell")
grafo_tierra_media.agregar_vertice("Minas Tirith")
grafo_tierra_media.agregar_vertice("Gondor")
grafo_tierra_media.agregar_vertice("Moria")

grafo_tierra_media.agregar_arista("Rivendell", "Minas Tirith", 50)
grafo_tierra_media.agregar_arista("Rivendell", "Gondor", 30)
grafo_tierra_media.agregar_arista("Minas Tirith", "Gondor", 20)
grafo_tierra_media.agregar_arista("Gondor", "Moria", 40)


inicio = "Rivendell"
fin = "Minas Tirith"
distancia = dijkstra(grafo_tierra_media, inicio, fin)


print(f"La distancia más corta es: {distancia}")

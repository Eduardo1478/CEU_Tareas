import math

class Estrella:
    def __init__(self, nombre, posX = 0, posY = 0, posZ = 0):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} en coordenadas ({self.posX}, {self.posY}, {self.posZ})"
    
    def distancia(self, otra_estrella):
        dx = self.posX - otra_estrella.posX
        dy = self.posY - otra_estrella.posY
        dz = self.posZ - otra_estrella.posZ
        distancia = math.sqrt(dx**2 + dy**2 + dz**2)
        return distancia
    
    def galaxia(self):
        if self.posX >= 0 and self.posY >= 0 and self.posZ >= 0:
            return "galaxia V"
        elif self.posX <= 0 and self.posY <= 0 and self.posZ <= 0:
            return "galaxia III"
        elif self.posX > 0 and self.posY > 0 and self.posZ < 0:
            return "galaxia I"
        elif self.posX < 0 and self.posY > 0 and self.posZ < 0:
            return "galaxia II"
        elif self.posX > 0 and self.posY < 0 and self.posZ < 0:
            return "galaxia IV"
        elif self.posX < 0 and self.posY > 0 and self.posZ > 0:
            return "galaxia VI"
        elif self.posX < 0 and self.posY < 0 and self.posZ > 0:
            return "galaxia VII"
        elif self.posX > 0 and self.posY < 0 and self.posZ > 0:
            return "galaxia VIII"
        else:
            return "galaxia desconocida"

        
estrella1 = Estrella("Estrella A", 2, 3, 1)
estrella2 = Estrella("Estrella B", 4, 4, 4)
estrella3 = Estrella( "Estrella C", -3, -1, 0)


print(str(estrella1) + " y " + estrella1.galaxia())
print(str(estrella2) + " y " + estrella2.galaxia())
print(str(estrella3) + " y " + estrella3.galaxia())

print("Distancia entre estrella A y B: " + str(estrella1.distancia(estrella2)))
print("Distancia entre estrella B y C: " + str(estrella2.distancia(estrella3)))




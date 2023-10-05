class Estrella:
    def __init__(self, posX = 0, posY = 0, posZ = 0):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ

    def __str__(self):
        return f"Estrella en coordenadas ({self.posX}, {self.posY}, {self.posZ})"
    
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

        
estrella1 = Estrella(2, 3, 1)
estrella2 = Estrella(4, 4, 4)
estrella3 = Estrella(-3, -1, 0)


print(str(estrella1))
print("estrella en: " + estrella1.galaxia())
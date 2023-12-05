class Mision:
    def __init__(self, tipo, reino, solicitante):
        self.tipo = tipo
        self.reino = reino
        self.solicitante = solicitante

class ComandanteThor:
    def __init__(self):
        self.valquirias_disponibles = 150
        self.unidades_disponibles = 5000

    def asignar_recursos(self, mision):
        print(f"Recibida misión: {mision.tipo} hacia {mision.reino} solicitada por {mision.solicitante}")

        if mision.solicitante in ['Odín', 'Loki']:
            print("Alta prioridad: asignando recursos adicionales.")
            self.valquirias_disponibles -= 5
            self.unidades_disponibles -= 10
            print(f"Recursos asignados - Valquirias: 5, Unidades: 10")

        else:
            self.valquirias_disponibles -= 2
            self.unidades_disponibles -= 5
            print(f"Recursos asignados - Valquirias: 2, Unidades: 5")
        
        print(f"Recursos restantes - Valquirias: {self.valquirias_disponibles}, Unidades: {self.unidades_disponibles}")



comandante_thor = ComandanteThor()


mision_1 = Mision("defensa", "Midgard", "Odín")
mision_2 = Mision("exploración", "Jotunheim", "Thor")
mision_3 = Mision("conquista", "Asgard", "Loki")

comandante_thor.asignar_recursos(mision_1)
comandante_thor.asignar_recursos(mision_2)
comandante_thor.asignar_recursos(mision_3)


while True:
    tipo = input("Ingrese el tipo de misión (defensa, exploración, conquista): ")
    reino = input("Ingrese el reino destino: ")
    solicitante = input("Ingrese el dios que solicitó la misión: ")

    nueva_mision = Mision(tipo, reino, solicitante)
    comandante_thor.asignar_recursos(nueva_mision)

    continuar = input("Si Desea agregar otra misión escriba si: ")
    if continuar.lower() != 'si':
        break
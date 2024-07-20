from models.animal import Animal

class Huron(Animal):
    def __init__(self, nombre: str, peso: float, edad: int):
        super().__init__(nombre, peso, edad)
        
    def hacer_sonido(self):
        return "¡Eek Eek!"
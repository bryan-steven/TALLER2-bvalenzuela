from models.ianimal import iAnimal, abstractmethod

class Animal(iAnimal):
    def __init__(self, nombre:str, peso:float, edad:int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    def obtener_nombre(self):
        return self._nombre

    def obtener_peso(self):
        return self._peso

    def obtener_edad(self):
        return self._edad
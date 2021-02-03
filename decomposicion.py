#decomponer consiste en decomponer los objetos en 
#partes mas pequeños

class Avion:
    def __init__(self, alcance, aerolinea, motores, marca, pasajeros):
        self.alcance = alcance
        self.aerolinea = aerolinea
        self.motores = motores
        self.marca = marca
        self.pasajeros = pasajeros
        self._consumo = Consumo('gasolina', 987)

    
    def repostar(self):
        if self.pasajeros > 200:
            return self._consumo.combustible(5465)
        else:
            return self._consumo.combustible(65465)




class Consumo:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad

    def combustible(self, cantidad):
        return f'has hechado {cantidad}'


RyanAir = Avion(987,'Ryanair',2,'Airbus',250)
print(RyanAir.repostar())

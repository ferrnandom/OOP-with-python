#decomponer consiste en decomponer los objetos en 
#partes mas pequeños

# class Automovil:
#     def __init__(self, modelo, marca, color):
#     #variables de instancia
#         self.modelo = modelo 
#         self.marca = marca
#         self.color = color 
#         self._estado = 'en reposo'
#         self._motor = Motor(cilindros = 4)
#     #estas dos ultimas variables son variables privadas

#     def acelerar(self, tipo='despacio'):
#         if tipo == 'rapida':
#             self._motor.inyecta_gasolina(10)
#         else:
#             self._motor.inyecta_gasolina(3)
#         self.estado = 'movimiento'

# class Motor:                       #tipo es un default keyword, un parametro por defecto
#     def __init__(self, cilindros, tipo='gasolina'):
#         self.cilindros = cilindros
#         self.tipo = tipo
#         self._temperatura = 0


#     def inyecta_gasolina(self, cantidad):
#         pass

class Avion:
    def __init__(self, motores, pasajeros, marca, modelo):
        self.motores = motores
        self.pasajeros = pasajeros
        self.marca = marca
        self.modelo = modelo


    def despegar(self, tipo = 'rapido'):
        



class Motor:
    def __init__(self, marca, potencia=alta):
        self.marca = marca
        self.potencia = potencia

    def repostar(self,cantidad):
        print('estamos repostando todo')
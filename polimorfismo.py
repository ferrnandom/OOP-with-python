# class Persona:
#     def __init__(self, nombre):
#         #inicializamos la variable de instancia
#         self.nombre = nombre 

#     def avanza(self):
#         print(f' Hola sou {self.nombre} y ando caminando')

# #clase ciclista extiende persona
# class Ciclista(Persona):

#     def __init__(self, nombre):
#         #inicializamos la superclase
#         super().__init__(nombre)

#     #este es el mismo metodo que el de la clase Persona
#     #solo que en este caso lo modifico
#     def avanza(self):
#         print(f' Hola, soy {self.nombre} y ando moviendome en mi bicicleta')

# #def main():
#     # persona = Persona('antonio')
#     # print(persona.avanza())

#     # ciclista = Ciclista('alajd')
#     # print(ciclista.avanza())


# if __name__ == '__main__':
#     #main()
#     fernando = Persona('fernando')
#     fernando.avanza()


#     alfonso = Ciclista('ciclista')
#     alfonso.avanza()


class Animal:
    def __init__(self, especie, comida):
        self.especie = especie
        self.comida = comida

    def comer(self):
        print(f'Hola soy un {self.especie} un animal {self.comida} y por lo tanto solo como hierbas')

#clase perro extiende a animal
class Perro(Animal):
    def __init__(self, especie, comida):
        super().__init__(especie, comida)

    #aqui modifico el metodo
    def comer(self):
        print(f'Hola, soy un {self.especie} un animal {self.comida} y por lo tanto solo como carne')


if __name__ == '__main__':
    jirafa = Animal('jirafa', 'herbivoro')
    jirafa.comer()

    tina = Perro('perro', 'carnivoro')
    tina.comer()
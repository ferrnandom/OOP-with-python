# class Rectangulo:
#     def __init__(self,base, altura):
#         self.base = base
#         self.altura = altura

#     def area(self):
#         return self.base * self.altura


# #para indicarle a python  que esta es una subclase de
# #la superclase Rectangulo escribimos en parentesis
# #el nombre de la super clase. La subclase hereda
# #el comportamiento de la superclase
# class Cuadrado(Rectangulo):
# #la forma en la que leemos esta linea de codigo es
# #la clase cuadrado extiende a rectangulo
#     def __init__(self,lado):
#         super().__init__(lado,lado)
#         #esta funcion nos permite obtener una referencia
#         #directa a la superclase. Esto es algo que siempre tengo q
#         #que hacer, siempre que inicialice una subclase tengo
#         #que inicializar la superclase.
# if __name__ == '__main__':
#     rectangulo = Rectangulo(5,10)
#     print(rectangulo.area())

#     cuadrado = Cuadrado(5)
#     print(cuadrado.area())



# class Animal:
#     def __init__(self, especie, velocidad):
#         self.especie = especie
#         self.velocidad = velocidad

#     def hablar(self):
#         return f'hello, I am a {self.especie} and I can reach a speed of {self.velocidad} per hour'


# class Perro(Animal):
#     def __init__(self, especie, velocidad):
#         super().__init__(especie, velocidad)#aqui le paso los parametros de la clase al constructor al que hago referencia

# if __name__ == '__main__':
#     animal = Animal('lobo', 20)
#     print(animal.hablar())
#     perro = Perro('perro', 8)
#     print(perro.hablar())



class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def presentarse(self):
        return f'hola amigos, me llamo {self.nombre} {self.apellidos} y tengo {self.edad}'

class Antonio(Persona):
    def __init__(self, nombre, apellidos,edad):
        super().__init__(nombre,apellidos, edad)


if __name__ == '__main__':
    persona = Persona('fernando', 'moyano', 987)
    print(persona.presentarse())

    antonio = Antonio('antonio','aldf',564)
    print(antonio.presentarse())
    
#en python los setters y los getters nos sirven para
#asegurar la encapsulacion de codigo, es decir,
#que si una varable es privada, solo yo pueda acceder 
#a ella.

class Persona:
    def __init__(self, nombre, edad, peso):
        self._nombre = nombre
        self._edad = edad
        self._peso = peso

    @property
    #aqui estoy definiendo el guetter
    def nombre(self):
        return self._nombre
    @nombre.setter
    #aqui defino al setter
    def nombre(self, value):
        print(f'the actual name {self._nombre} is gonna change to... ')
        print(value)
        

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, value):
        if value < 0:
            print('you are weird')


fernando = Persona('Fernando', 18, 62)
print(fernando.nombre)
fernando.nombre = 'Antonio'#aqui modifico el atributo de nombre
print(fernando.nombre)
print(fernando.edad)
fernando.edad = -1
#print(fernando.edad)
    






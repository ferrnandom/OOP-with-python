#en python los setters y los getters nos sirven para
#asegurar la encapsulacion de codigo, es decir,
#que si una varable es privada, solo yo pueda acceder 
#a ella.




class Persona:
    def __init__(self,  nombre, apellidos):
        self.nombre = nombre
        self._edad = None
        self.apellidos = apellidos 
    
    #este es el guetter, el cual se encarga de obtener
    #el valor valor.
    @property
    def mayoria_edad(self):
        return self._edad

    @mayoria_edad.setter
    def mayoria_edad(self, value):#value es la funcion anterior
        if value < 0:
            print('you are weird')


if __name__ == '__main__':
    fernando = Persona(  'Fernando', 'Moyano')
    fernando.mayoria_edad = -5
    print(fernando.mayoria_edad)






# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def saluda(self, otra_persona):
#         print(f'hola {otra_persona.nombre}, me llamo {self.nombre}')



# antonio = Persona('antonio', 20)
# pepe = Persona('pepe', 24)

# antonio.saluda(pepe)

# class Coordenada:

#     def __init__(self, x, y):
#       self.x = x
#       self.y = y

#     def distancia(self, otra_coordenada):
#         x_diff = (self.x - otra_coordenada.x)**2
#         y_diff = (self.y - otra_coordenada.y)**2

#         return (x_diff + y_diff) ** 0.5

# if __name__ == '__main__':
#     coordenada_1 = Coordenada(20, 50)
#     coordenada_2 = Coordenada(25, 80)
    
#     print(coordenada_1.distancia(coordenada_2))








#inicializamos la clase
class Estudiantes:
    #inicializamos el cosntructor   #aqui escribimos sus parametros(caracteristicas)
    def __init__(self, nombre, apellido, media):
        self.nombre = nombre
        self.apellido = apellido
        self.media = media


    #estos son los metodos de la clase, es decir
    #las funciones que puede hacer

    def presentarse(self, otro_alumno): #con el objeto otro_alumno tengo que especificar que atributo quiero ex: otro_alumno.nombre
        return f'Hola {otro_alumno.nombre} {otro_alumno.apellido}, me llamo {self.nombre} {self.apellido} y mi nota media es {self.media}'


if __name__ == '__main__':
    fernando = Estudiantes('fernando', 'moyano', 465465)
    antonio = Estudiantes('antonio', 'adjka', 46546)

    print(fernando.presentarse(antonio))

























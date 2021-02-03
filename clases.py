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

























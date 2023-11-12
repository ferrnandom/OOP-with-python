
class Avion:
    def __init__(self, motores, marca, aerolinea, alcance):
        self.motores = motores
        self.marca = marca
        self.aerolinea = aerolinea
        self.alcance = alcance
    
    #metodo
    def despegar(self):
        #estos son metodos que estan dentro de este metodo
        #se llaman metodos de primera clase y se ejecutan
        #cuando ejecuto al metodo principal
        self.avisar()
        self.acelerar()
        self.levantar()
        self.estabilizar()
        self.velocidad_crucero()
        
        return f'hola a todos los pasajeros y gracias por elegir {self.aerolinea} para volar'

    def avisar(self):
        return 'abrochence los cintirones'
    def acelerar(self):
        return 'alcanzando velocidad de 290 km/h'
    def levantar(self):
        return 'levantando el morro'
    def estabilizar(self):
        return 'estabilizando el avion'
    def velocidad_crucero(self):
        return 'alcanzando la velocidad crucero'

if __name__ == '__main__':
    avioncito = Avion(4,"Boeing","Ryanair", 8786)
    print(avioncito.despegar())
    print(avioncito.avisar())
    print(avioncito.acelerar())
    print(avioncito.levantar())
    print(avioncito.estabilizar())
    print(avioncito.velocidad_crucero())

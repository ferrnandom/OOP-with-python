class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        return f'llenando agua con la temperatura {temperatura}'

    def _añadir_jabon(self):
        return 'añadiendo jabon'
    
    def _lavar(self):
        return 'lavando'

    def _centrifugar(self):
        return 'estamos centrifugando tu ropa'



if __name__ == "__main__":
    lavadora = Lavadora()
    print(lavadora._llenar_tanque_de_agua('fria'))
    print(lavadora._añadir_jabon())
    print(lavadora._lavar())
    print(lavadora._centrifugar())
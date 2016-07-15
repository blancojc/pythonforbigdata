class CuerpoRedondo(object):

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio < 0 :
            raise ValueError("radio deber ser un numero positivo")
        self._radio = radio


from math import pi

class Esfera(CuerpoRedondo):
  
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 4 * pi * self.radio ** 2

    def volumen(self):
        return 4/3 * ( pi * self.radio ** 3)
        
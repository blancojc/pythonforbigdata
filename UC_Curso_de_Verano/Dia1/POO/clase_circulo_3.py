class Circulo(object):

    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio < 0 :
            raise ValueError("radio deber ser un numero positivo")
        self._radio = radio
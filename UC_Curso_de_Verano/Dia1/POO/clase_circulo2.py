class Circulo(object):

    PI = 3.1415926535889793

    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return self.PI * (self.radio ** 2)

circulo=Circulo(4.5)
circulo.area()
        
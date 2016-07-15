class Persona(object):
    
    def __init__(self, nombre, password):
        self.nombre = nombre
        self._password = password

    def password(self):
        return self._password

person = Persona("Carlos","XCVWRD2")
person.nombre
person.password()

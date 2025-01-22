# creamos la clase padre
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print('Soy un animal del tipo ', type(self).__name__)

# la clase perro hereda de la clase animal
# Creamos una clase hija que hereda de la clase padre


class Perro(Animal):
    def __init__(self, especie, edad, dueno):
        super().__init__(especie, edad) # en esta funcion solamente se llama los atributos del padre.
        self.dueno = dueno


    def hablar(self):
        print('Guau!')

    def moverse(self):
        print('Caminando con 4 patas')



class Vaca(Animal):

    def hablar(self):
        print('Muuuu!')


    def moverse(self):
        print('Caminando con 4 patas')


class Abeja(Animal):

    def hablar(self):
        print('Bzzz!')

    def moverse(self):
        print('Volando')


    def picar(self):
        print('Picar')

mi_perro = Perro('Mamifero', 10, 'Moralens')
print(mi_perro.especie) # accedemos a un atributo de la clase padre, #Mamifero 
mi_perro.describeme() # Soy un animal del tipo  Perro

mi_vaca = Vaca('Mamifero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()
mi_vaca.hablar()

mi_vaca.describeme()
mi_perro.describeme()

mi_abeja.picar()



# de esta forma podemos confirmar que la clase perro es hija de la clase
# Animal
print(Perro.__base__)  # <class '__main__.Animal'>

# podemos ver que clases descienden de una en concreto con __subclasses__
print(Animal.__subclasses__())  # [<class '__main__.Perro'>]



# HERENCIA MULTIPLE

class Clase:
    pass

class Clase1:
    pass

class Clase2(Clase, Clase1):
    pass
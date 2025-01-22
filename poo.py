'''Creamos una clase'''
class Dog:
    especie = 'mamifero' # atributo de clase
    '''Creamos el constructos'''
    def __init__(self, nombre, raza):
        print(f'Creando perro {nombre}, {raza}')
        # self es una variable que representa la instancia de una clase

        # Atributo de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print('Guau, Guau')


    def caminar(self, pasos):
        print(f'The dog walk {pasos} steps')

# creamos una instancia de la clase(un objeto)
my_dog = Dog(nombre= 'Tom', raza= 'Bulldog') # creamos el objeto perro
print(type(my_dog))
# <class '__main__.Perro'>
print(my_dog.nombre) # de esta forma accedemos a los atributos de la instancia de la clase

print(my_dog.raza) # Bulldog
print(my_dog.nombre) # Tom

print(Dog.especie) # mamifero

mi_especie = my_dog.especie
print(mi_especie) # mamifero

# llamamos a la funcion ladrar y caminar

my_dog.ladra() # Guau, Guau
my_dog.caminar(10) # The dog walk 10 steps




 

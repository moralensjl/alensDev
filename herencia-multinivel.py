''''  HERENCIA MULTINIVEL  '''

class Abuelo:
    def __init__(self, nombreAbuelo= None):
        self.__nombre = nombreAbuelo
        print('Clase Abuelo')

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre


    def lenguajeDeAbuelo(self):
        print(self.__nombre, 'Programa en Ensamblador')



    def __str__(self):
        return f'Nombre del Abuelo {self.__nombre}'



class Padre(Abuelo):
    def __init__(self, nombrePadre= None, nombreAbuelo= None):
        super().__init__(nombreAbuelo)
        self.__nombre = nombrePadre
        print('Padre Creado')


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre


    def lenguajeDePadre(self):
        print(self.__nombre, 'Programa en C')


    def __str__(self):
        return super().__str__() + f'\nNombre del padre {self.__nombre}'
    


class Hijo(Padre):
    def __init__(self, nombreHijo, nombrePadre=None, nombreAbuelo=None):
        super().__init__(nombrePadre, nombreAbuelo)
        self.__nombre = nombreHijo
        print('Hijo creado')


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre


    def lenguajeDeHijo(self):
        print(self.__nombre, 'Programa en Python')


    def __str__(self):
        return super().__str__() + f'\nNombre del Hijo {self.__nombre}'
    

if __name__ == '__main__':

    # Creamos un objeto de la clase Abuelo y probamos sus metodos 
    print('=== ABUELO ===')
    abuelo = Abuelo('Fran')
    print(abuelo) # Metodo __str__
    print(abuelo.nombre) # Metodo getter
    abuelo.nombre = 'Francisco' # Metodo setter
    print(abuelo)

    # Creamos un objeto de la clase Padre y probamos sus metodos
    print('\n=== PADRE ===')
    padre = Padre('Carlos', 'Francisco')
    print(padre)


    print('\n=== HIJO ===')
    hijo = Hijo('Pablo', 'Carlos', 'Francisco')
    print(hijo)

    # Comprobamos que desde la ultima clase (Hijo) podemos acceder a
    # metodos de su padre (Padre) y de su abuelo (Abuelo)
    print('\n=== LENGUAJES DE PROGRAMACION ===')
    print(hijo.lenguajeDeAbuelo())
    print(hijo.lenguajeDePadre())
    print(hijo.lenguajeDeHijo())
    print(abuelo.lenguajeDeAbuelo())
    print(hijo.lenguajeDeAbuelo())
    print(padre.lenguajeDePadre())
    print()

    ### Metodo MRO 
class Class1:
    def m(self):
        print('En class1')

class Class2(Class1):
    def m(self):
        print('En class2')
        super().m()


class Class3(Class1):
    def m(self):
        print('En class3')
        super().m()


class Class4(Class2, Class3):
    def m(self):
        print('En class4')
        super().m()


obj = Class4()
print(obj)
print(obj.m())

print(Class4.mro())
# [<class '__main__.Class4'>, <class '__main__.Class2'>,
#  <class '__main__.Class3'>, <class '__main__.Class1'>, 
# <class 'object'>]


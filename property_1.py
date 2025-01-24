# Creamos una clase
class Persona:
    '''Creamos el constructor de la clase Persona'''
    def __init__(self, nombre, identificador):
        self.__nombre = nombre
        self.__identificador = identificador


    # Encapsulamos las variables con get y set
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor


    @property
    def identificador(self):
        return self.__identificador
    

    @identificador.setter
    def identificador(self, valor):
        self.__identificador = valor


    def __str__(self):
        return f'Mi nombre es {self.__nombre} y mi ID {self.__identificador}'

# creamos varios objetos de persona
mi_persona = Persona('James', 100) 
print(mi_persona) # Mi nombre es James y mi ID 100. ** Al poner un print() se sobreescribe el 
# metodo __str__**
mi_persona2 = Persona('Martha', 101)
print(mi_persona2) # Mi nombre es Martha y mi ID 101.** antes de modificar el nombre a 'Sara' **

# accedemos a los atributos de la clase con get
nombrePersona = mi_persona.nombre
print(nombrePersona) # James
print(mi_persona.nombre)

# modificamos el valor del atributo con set
mi_persona2.nombre = 'Sara'
nuevoNombre = mi_persona2.nombre
print(nuevoNombre) # Sara

    
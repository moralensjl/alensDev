class Persona:
    def __init__(self, nombre, apellido, identificador):
        self.nombre = nombre
        self.apellido = apellido
        self.__identificador = identificador
        print('Creamos la clase persona')


    @property
    def identificador(self):
        return self.__identificador


    @identificador.setter
    def identificador(self, nuevo):
        self.__identificador = nuevo


    def __str__(self):
        return f'Mi nombre es {self.nombre}'
    

persona1 = Persona('Jarl', 'Erickson', '001')
persona2 = Persona('Julliete', 'Silverton', '002')
persona3 = Persona('Sara', 'Monroe', '003')

print(persona1.identificador) # de esta forma accedemos a los atributos privados de una clase


class CuentaUsuario(Persona):
    def __init__(self, nombre, apellido, identificador, nombre_usuario, contrasena):
        super().__init__(nombre, apellido, identificador)
        self.nombre_usuario = nombre_usuario
        self.__contrasena = contrasena
        print('Clase Cuenta usuario creada')


    @property
    def contrasena(self):
        return self.__contrasena
    

    @contrasena.setter
    def contrasena(self, nuevo):
        self.__contrasena = nuevo



    def __str__(self):
        return f'{self.nombre}, {self.apellido}, {self.identificador}, {self.nombre_usuario} {self.__contrasena} '
    # no podemos acceder a los atributos privados con los guiones bajos __
    


usuario1 = CuentaUsuario('Nathaly', 'Gomes', '004', '@nathalyGs', '09gomes')
usuario2 = CuentaUsuario('Peter', 'Rubel', '005', '@peterR90', 'Rubel2304') 
usuario3 = CuentaUsuario('Fernanda', 'Rinza', '006', 'Fernan_rinza14', 'rinza1404')
print(usuario1.nombre_usuario)


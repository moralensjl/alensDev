class Biblioteca:
    nombreBiblioteca = 'Biblioteca de Barcelona' 
    # creamos un atributo de clase que se va a asignar a todos los objetos
    def __init__(self,  lista_de_libros ):
        self.lista_de_libros = lista_de_libros
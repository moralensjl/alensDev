# HERENCIA MÚLTIPLE

class A:
    def __init__(self):
        print('Soy de clase A')
        
    def a(self):
        print('Este metodo lo heredo de A')


class B:
    def __init__(self):
        print('Soy una clase B')

    def b(self):
        print('Este metodo lo heredo de B')


class C(A, B): # La clase principal sera la clase mas a la izquierda.
    def __init__(self):
        super().__init__()

    def c(self):
        print('Este metodo es de C')


c = C()
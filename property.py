'''
Decorador Property
'''
class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo


    @property
    def mi_atributo(self):
        return self.__mi_atributo
    

    @mi_atributo.setter
    def mi_atributo(self, valor):
        if valor != '':
            print('Modificando el valor')
            self.__mi_atributo = valor
    

mi_clase = Clase('Mi atributo') # creamos un objeto
clase = mi_clase.mi_atributo # para imprimir el valor por pantalla defino una variable
print(clase) # Mi atributo. imprime por pantalla el objeto **mi_clase**

# modificando el valor de la clase
mi_clase = Clase('Atributo valor')
mi_clase.mi_atributo = 'Nuevo atributo' # **modificamos el valor del objeto de la clase**
nueva_clase = mi_clase.mi_atributo
print(nueva_clase) # Nuevo atributo 

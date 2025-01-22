class Clase:

    def metodo(self):
        return 'Método normal', self
    
    @classmethod
    def metodoClase(cls): # cls es el argumento
        return 'Método de clase', cls
    # acceden a la clase directamente. no acceden a la instancia. 
    

    @staticmethod
    def metodoestatico():
        return 'Método estatico'
    
print( Clase.metodoClase()) # ('Método de clase', <class '__main__.Clase'>)

# tambien se pueden llamar sobre el objeto
# mi_clase = Clase('clase')
# mi_clase.metodoClase()

# Los metodos de clase:
# no pueden acceder a los atributos de clase
# pero si pueden modificar los atributos de la clase

Clase.metodoestatico()
libro = {'nombre': 'Pinocho',
         'autor': 'Carlo Collodi',
         'añoLanzamiento': 1982,
         'paginas': 863,
         'ediClin': True,
         'E-Libro': False 
         }

print(libro)
# {'nombre': 'Pinocho',
#  'autor': 'Carlo Collodi',
#  'añoLanzamiento': 1982, 
# 'paginas': 863,
# 'ediClin': True,
# 'E-Libro': False}

# Acceder a un elemento de un diccionario

print(libro['autor']) # Carlo Collodi

# Agregar elemento a un diccionario
libro['Genero'] = 'Novela'
print(libro)

# Borrar un elemento del dict
del libro['paginas']
print(libro)

# comprobar si un elemento esta en el dict
comprobacion = 'autor' in libro # True
print(comprobacion)

# Pedir las llaves del dict
keys = libro.keys() # dict_keys(['nombre', 'autor', 'añoLanzamiento', 'ediClin', 'E-Libro', 'Genero'])
print(keys)

# Pedir los valores del dict
values = libro.values() # dict_values(['Pinocho', 'Carlo Collodi', 1982, True, False, 'Novela']
print(values)

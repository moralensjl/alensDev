nombres = ['Pedro', 'Cecilia', 'Maria', 'Miguel']
print(nombres[:]) # ['Pedro', 'Cecilia', 'Maria', 'Miguel']
print(nombres[0:]) # ['Pedro', 'Cecilia', 'Maria', 'Miguel']
print(nombres[1:]) # ['Cecilia', 'Maria', 'Miguel']
print(nombres[:3]) # ['Pedro', 'Cecilia', 'Maria']
# Para saber el indice de un elemento
print(nombres.index('Cecilia')) # 1
nombres.append('Alens')
print(nombres) # ['Pedro', 'Cecilia', 'Maria', 'Miguel', 'Alens']

# Eliminar un elemento de la lista
nombres.pop(3)
print(nombres) # ['Pedro', 'Cecilia', 'Maria', 'Alens']

# Modificar un elemento de lista
nombres[2] = 'Gabriela'

# Lista de alumnos
alumnos = [
    ['Adriana', 13, 9.3],
    ['Elias', 12, 9.2 ]
]

print(alumnos[0]) # ['Adriana', 13, 9.3]
print(alumnos[1]) # ['Elias', 12, 9.2]
print(alumnos[0][2]) # 9.3
print(f'La alumna {alumnos[0][0]} tiene un promedio de {alumnos[0][2]}')
# La alumna Adriana tiene un promedio de 9.3
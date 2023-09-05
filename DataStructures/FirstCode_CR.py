#################LISTAS####################

my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
print(my_lista)                             #Imprime la lista previa.
print(type(my_lista))                       #Imprime el tipo de la lista.
print(my_lista[2])                          #Imprime la posición 2 de la lista (Aclarando que las posiciones van de 0 a n).

print("my_lista size: ", len(my_lista))     #Imprime el tamaño de lista, ene ste caso tiene 6 elementos.
print(my_lista[0:2])                        #Imprime desde la posición 0 hasta la anterior al número que se colocó de segundas.
print(my_lista[:2])                         #Imprime desde el primer elemento de la lista hasta el anterior que se colocó.

my_lista.append('Blanco')                   #Se grega elemento al final de la lista.
print(my_lista)                             #Se imprime la la última versión de la lista, es decir añadiendo el color blanco.

my_lista.insert(3, 'Negro')                 #Se agrega un nuevo elemento a la lista aclarando la posición en que lo queremos.
print(my_lista)                             #Se imprime la la última versión de la lista, es decir añadiendo el color negro en la posición 3.

my_lista.extend(['Marron', 'Gris'])         #Concatena a otra lista.
print(my_lista)                             #Se imprime la la última versión de la lista.

print(my_lista.index('Azul'))               #Indica la posición en que se encuentra el color.

my_lista.remove('Marron')                   #Se elimina un elemento de la lista.
print(my_lista)

my_lista.insert(8, 'Marron')
print(my_lista)

print(my_lista.pop())                       #Imprime el último elemento.
size = len(my_lista)
print("size = ", size)

my_lista_3 = my_lista*3                     
print("my_lista_3: ", my_lista_3)           #Imprime la lista tres veces.

print("Sort:")                              #Se usa para organizar numéricamente, en este caso no aplica.
print()
my_listaSort = my_lista.sort()
print(my_listaSort)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()                           #En este caso el uso de la función Sort sí se apica, pues la lista es numérica.
print(my_NumList)

my_NumList.sort(reverse = True)             #Ordena la lista de mayor a menor.
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("######### TUPLAS ##########")
print("###########################")
print("###########################")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
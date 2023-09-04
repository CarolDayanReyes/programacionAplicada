#Imprimir los números primos existentes entre 0 y 30
tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1


#¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/o continue para tal fin
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1

#¿Es posible saber en qué medida se optimizó?
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))


ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')

#Si la cantidad de números que se evalúa es mayor a treinta, ¿esa optimización crece?
tope_rango=100
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')
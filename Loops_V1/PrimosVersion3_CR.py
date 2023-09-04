a = 1
value = input('\nIngrese un valor para saber si es primo o no:')
value = int(value)

while a == 1:
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
    
    if conta == 2:
       print("\n")
       print(f'{i} SÍ un primo.')
       print("\n")
    else:
       print("\n")
       print(f'{i} NO es un primo.')
       print("\n")

    print('¿Desea continuar? Oprima el número 1 si la respuesta es afirmativa.')
   
    a = input()
    a = int(a)

    if a != 1:
        break
    

    value = input('Ingrese un valor para saber, nuevamente, si es primo o no.')
    value = int(value)
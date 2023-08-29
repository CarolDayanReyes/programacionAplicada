def detector_primos(primos):
    return primos

p = 1
detector_primos = int(input('\nIngrese un valor para saber si es primo: '))
print("\n")

while p == 1:
    for i in range(1,detector_primos+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
            
    if conta == 2:
       print(f'{i} efectivamente es un primo.')
       print("\n")
    else:
       print(f'{i} lastimosamente no es un primo.')
       print("\n")

    print('¿Deseas averiguar si otro número es primo?. Escribe 1 si la respuesta es afirmativa de lo contrario envía cualquier otro NÚMERO.')
    p = int(input())

    if p != 1:
        break

    detector_primos = int(input('\nIngrese un valor para saber nuevamente si es primo: '))
    print("\n")
    
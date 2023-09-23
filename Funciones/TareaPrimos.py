while True:    
     def procPrimo(primo): 
         print('1 efectivamente es primo') 
         for i in range(2,primo+1): 
             conta = 0 
             for n in range(2, primo+1): 
                 residue = i%n 
                 if residue == 0: 
                     conta = conta + 1 
             if conta == 1: 
                         print(f'{i} efectivamente es primo') 
             else: 
                         print(f'{i} NO es primo') 
         return "¡RANGO FINALIZADO!"  
     primo=int(input('Ingrese el rango hasta el cuál desea saber los números primos: ')) 
     print(procPrimo(primo)) 
     y=int(input("Para continuar digite cualquier número entero y para finalizar digite el número 1: ")) 
     if y==1: 
         break
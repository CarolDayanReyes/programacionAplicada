while True: 
     def procFact(factorial): 
         if factorial==1: 
             return 1 
         else: 
             return factorial * procFact(factorial-1) 
     factorial=int(input('Digite el límite del rango: ')) 
     print(procFact(factorial)) 
     y=int(input("Para finalizar digite el número 1 y para continuar cualquier otro número entero: ")) 
     if y==1: 
         break
def detector_factorial(factorial):
    return factorial

while True:

    detector_factorial = int(input("Enter a positive integer value: "))
    print("Valor: ", detector_factorial)
    a = isinstance(detector_factorial, int)
    if a == True and detector_factorial > 0:
        fact = 1
        for i in range (1, detector_factorial + 1):
            fact = fact*i            
        print(f'The factorial of {detector_factorial} is: ', fact)
    else:
        print("Please, enter a positive integer number")
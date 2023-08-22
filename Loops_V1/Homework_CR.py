a = input("\nIngresa un numero para a: ")
a = int(a)
b = input("\nIngresa un numero para b: ")
b = float(b)
c = a + b

if a == b:
    print("\nSon iguales")
else:
    print("\nSon diferentes")

print("\nEl tipo de a es: ", type(a))
print("El tipo de b es: ", type(b))
print("\nc es la suma de a y b por ende es igual a ", c)

if type(a) == type(b):
    print("\na y b son de igual tipo.\n")
else:
    print("\na y b son de diferente tipo.\n")
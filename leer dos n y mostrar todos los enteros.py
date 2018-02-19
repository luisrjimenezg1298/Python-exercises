print("   Leer dos números y mostrar todos los enteros comprendidos entre ellos")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

enteros = 0

if num1 < num2:
    print("Todos los enteros comprendidos entre ",num1," y ",num2," son: ")
    for enteros in range (num1+1,num2):
        print(enteros)

if num2 < num1:
    print("Todos los enteros comprendidos entre ",num2," y ",num1," son: ")
    for enteros in range (num2+1,num1):
        print(enteros)
        
input("Fin")

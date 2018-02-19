print("Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
terminados = 0

print("Todos los numeros terminados en 4 comprendidos entre ",num1," y ",num2," son: ")

if num1 < num2:
    for terminados in range (num1+1,num2):
        if terminados % 10 == 4:
            print(terminados)

if num2 < num1:
    for terminados in range (num2+1,num1):
        if terminados % 10 == 4:
            print(terminados)
            
input("Fin")

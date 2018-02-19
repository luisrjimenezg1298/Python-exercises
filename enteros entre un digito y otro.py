print("Leer un numero entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro")

numero = input("Ingrese un numero entero de dos digitos: ")
lista = list(map(int, numero))
dig1 = lista[0]
dig2 = lista[1]

print("Todos los enteros comprendidos entre ")

if dig1 < dig2 :
    for enteros in range(dig1+1,dig2):
        print(enteros)

if dig2 < dig1 :
    for enteros in range(dig2+1,dig1):
        print(enteros)
        
input("Fin")



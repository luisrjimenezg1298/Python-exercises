print("Leer un número entero de 3 dígitos y determinar si tiene el dígito 1")

numero = input("Ingresar un numero entero de tres digitos: ")
lista = list(map(int,numero))
dig1 = lista[0]
dig2 = lista[1]
dig3 = lista[2]

if (dig1 == 1) or (dig2 == 1) or (dig3 ==1):
    print("El numero tiene el digito 1.")

else:
    print("El numero no tiene el digito 1.")

input("Fin")


    

print("Leer un número entero y mostrar en pantalla su tabla de multiplicar")

numero = int(input("Ingrese un numero entero: "))

for mult in range (1,13):
    producto = numero * mult
    print(numero,"*",mult," = ",producto)

input("Fin")

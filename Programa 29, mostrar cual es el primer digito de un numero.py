print("Leer un número entero y determinar a cuánto es igual el primero de sus dígitos")

numero = int(input("Ingresar un numero entero: "))
ultdig = 0

print("El primero de sus digitos es: ")

while numero != 0 :
    ultdig =  int(numero - int(numero / 10) * 10)
    numero = int(numero / 10)

print(ultdig)

input("\nFin")
    

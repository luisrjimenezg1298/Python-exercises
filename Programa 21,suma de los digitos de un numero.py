print("Leer un número entero y determinar a cuánto es igual la suma de sus dígitos")

numero = int(input("Ingresar un numero entero: "))
ultdig = 0
suma = 0

print("La suma de los digitos de ",numero," es igual a: ")

while numero != 0 :
    ultdig = int(numero - int(numero / 10) * 10)
    suma = int(suma + ultdig)
    numero = int(numero / 10)

print(suma)

input("Fin")

print("Leer dos números enteros y determinar a cuánto es igual el producto mutuo del primer dígito de cada uno")

numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero: "))
ultdig1 = 0
ultdig2 = 0

while numero1 != 0 :
    ultdig1 =  int(numero1 - int(numero1 / 10) * 10)
    numero1 = int(numero1 / 10)

while numero2 != 0 :
    ultdig2 =  int(numero2 - int(numero2 / 10) * 10)
    numero2 = int(numero2 / 10)

producto = ultdig1 * ultdig2

print("El producto mutuo del primer dígito de cada numero es : ", producto)

input("Fin")

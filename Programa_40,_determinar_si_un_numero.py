print("Leer un número de dos dígitos y determinar si pertenece a la serie de Fibonacci.")

numero = int(input("Ingrese un numero entero de dos digitos:"))
var0 = int(0)
var1 = int(1)
suma = 0

for serie1 in range (3,100):
    suma = var0 + var1
    var0 = var1
    var1 = suma
    if suma == numero:
        print("El numero ",numero," pertenece a la serie de Fibonacci.")

print("Si no se le indica que pertenece es porque no pertenece.")

input("Fin")

print("Determinar a cuánto es igual la suma de los elementos de la serie de Fibonacci entre 0 y 100")

var0 = int(0)
var1 = int(1)
suma = 0
total = 0

print(var0)
print(var1)

for serie1 in range (3,100):
    suma = var0 + var1
    var0 = var1
    var1 = suma
    total = total + suma
    if suma < 100:
        print(total)

input("Fin")

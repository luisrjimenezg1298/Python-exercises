print("Utilizando el concepto de ciclo generar la serie de Fibonacci hasta llegar o sobrepasar el número 10000")
var0 = int(0)
var1 = int(1)
suma = 0

print(var0)
print(var1)

for serie1 in range (3,10000+1):
    suma = var0 + var1
    var0 = var1
    var1 = suma
    if suma <= 11000:
        print(suma)

input("Fin")


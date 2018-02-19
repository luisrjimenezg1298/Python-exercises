print("Leer un número entero y determinar cuántos dígitos tiene")

numero = input("Ingrese un numero entero: ")
lista = len(list(map(int,numero)))

print("El numero ",numero," tiene ",lista,"digito/s.")

input("Fin")

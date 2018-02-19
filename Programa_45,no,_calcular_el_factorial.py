print("Leer un número y calcularle el factorial a todos los enteros comprendidos entre 1 y el número leído")

numero = int(input("Ingrese un numero entero: "))
facto = 1
cont = 1
numerito = numero

while numerito != 0:
    for numerito in range (1,numero+1):
        if numerito < 0:
            print("El factorial no esta definido para numeros negativos.")
        else:
            for cont in range (1,numerito+1):
                facto = facto * cont
    print("El factorial del numero ",numerito," es: ",facto)
    
    
    
input("Fin")

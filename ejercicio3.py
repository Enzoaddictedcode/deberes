Ingresar un número validándolo como entero positivo. Mostrar todos los números primos menores o iguales al número ingresado.
Indicar cuantos valores están siendo mostrados y la suma de los números mostrados.

cont = 0
numero = int(input("Ingrese un numero a evaluar: "))
for n in range(1, numero + 1):
    for d in range(1, n + 1):
        if n % d == 0:
            cont += 1
    if cont == 2:
        print("{}".format(n), end=" ")
    cont = 0
print("Fin")

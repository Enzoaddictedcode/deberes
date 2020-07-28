 El costo de enviar por correo es de $300 para cartas que pesan menos de 30 grs. Y $5 por cada gramo adicional para cartas que pesan más de 30 grs. 
Leer un numero real el cual representará el peso de la carta y luego muestre el costo de enviar la carta.

correo = int(input("ingrese el peso de la carta :"))
costoorgian = 300
if  correo == 30:
    print("El valor a pagar es 300")

if correo > 30:
    resta = correo - 30
    multi = resta * 5
    suma= costoorgian + multi
print(f'Ek valor a pagar es {suma}')

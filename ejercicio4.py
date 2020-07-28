Simule emitir el total de una factura considerando lo siguiente: leer la cantidad, el nombre del artículo y el precio unitario,
Si el total bruto es mayor a $150,000 hacer un descuento del 2%, si es mayor a $300,00 hacer un 3% de descuento, 
no se puede hacer 2 descuentos. Finalmente agregar el 12% de IVA.

cantidad = float(input("ingrese la cantidad :"))
nameartic = input("Ingrese nombre del articulo :")
preciouni = float(input("Ingrese precio Unitario :"))

totbrut = cantidad * preciouni

if totbrut >= 150.000 <= 300.000:
    descuento = totbrut * 0.02
    suma=descuento + totbrut
    iva=totbrut * 1.12
    print(f"El valor es : {iva}")
elif totbrut < 150.000:
    ivai = totbrut * 1.12
    print(f"El valor es : {ivai}")

if totbrut > 300.000:
    descuento2 = totbrut * 0.03
    suma2=descuento + totbrut
    iva2=totbrut * 1.12
    print(f"El precio final es  : {iva2}")

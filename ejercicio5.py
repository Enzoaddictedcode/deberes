Elabore un diagrama de flujo que convierta las pulgadas a metros,
se conoce que una pulgada es igual a 2.54 cm el programa termina cuando se ingresa el 0 como valor de pulgada. 

def main():

    pulgadas = float(input("Escriba una cantidad de pulgadas: "))
    while pulgadas == 0:
        print("Programa finbalizado")
        break
        print("finalizado")
    metro = pulgadas * 0.0254

    print(f"{pulgadas} pulgadas son {metro} m")


if __name__ == "__main__":

    main()

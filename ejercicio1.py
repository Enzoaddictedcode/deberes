 Desarrolle un diagrama en el que se lea desde el teclado el nombre, edad, sexo y estado civil de una persona, e 
imprima el nombre solo si corresponde a un hombre casado mayor de 30 años o a una mujer soltera menor a 50 años.

nombre = input("Ingrese su nombre :")
edad = int(input("Ingrese su edad :"))
sexo =input("ingrese su sexo :")
stati =input("ingrese estado civil :")

ansexo = 'marcelino'
ansexo2 = 'femenino'

if edad > 30 and sexo == 'masculino':
    print(f'Hola '+nombre+' tienes '+str(edad) +' y eres de sexo '+sexo+' y eres '+stati)


if edad < 50 and sexo =='femenino' and stati == 'soltera':
    print(f'Hola '+nombre+' tienes '+str(edad) +' y eres de sexo '+sexo+' y eres '+stati)

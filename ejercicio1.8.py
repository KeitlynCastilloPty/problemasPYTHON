nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

nota1 = float(input("Ingresar la primera nota: "))
nota2 = float(input("Ingresar la segunda nota: "))
nota3 = float(input("Ingresar la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Nombre:", nombre)
print("Edad:", edad)
print("Promedio:", round(promedio, 2))

if promedio >= 71:
    print("Aprobado")
else:
    print("No aprobado")

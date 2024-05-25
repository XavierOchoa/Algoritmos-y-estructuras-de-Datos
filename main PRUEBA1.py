print("********* BIENVENIDOS AL BURGUER KING ********* ")
print("Ingrese los datos para la factura electrónica ")
print(" ")
nombre = input("Ingrese su nombre: ")
ced = input("Ingrese su número de cédula: ")
corr = input("Ingrese su correo: ")
amb = int(input("Ingrese el número de hamburguesas a adquirir: "))
print(" ")

ambsenc = 1.5
ambdob = 2.5
ambtrp = 3.25

print(" ")
print("Ingrese uno de los siguientes tipos de hamburguesas:")
print("1) Sencilla")
print("2) Doble")
print("3) Triple")
tipo = int(input("Ingrese la opción: "))

if tipo == 1:
    pf = amb * ambsenc
elif tipo == 2:
    pf = amb * ambdob
elif tipo == 3:
    pf = amb * ambtrp
else:
    print(" ")
    print("Este tipo de hamburguesa no existe")
    print("Muchas gracias")
    quit()
    
print(" ")
print("Ingrese su forma de pago")
print("1) Tarjeta de crédito")
print("2) Efectivo")
fp = int(input("Ingrese la opción: "))

if fp == 1:
    pf1 = pf * 1.05
elif fp == 2:
    pf1 = pf
else:
    print(" ")
    print("No existe este tipo de pago")
    print("Muchas gracias")
    quit()

print(" ")
print(f"Genial, {nombre}, el precio final es: ${round(pf1,2)}")
print(f"La factura se enviará a su correo {corr}")

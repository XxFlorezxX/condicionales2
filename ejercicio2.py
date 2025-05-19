edad = int(input("Ingrese su edad: "))
if edad < 10:
    print("Es un niño")
elif edad >= 10 and edad < 15:
    print("Es un preadolecente")
elif edad >= 15 and edad < 18:
    print("Es un adolecente")
elif edad >= 18 and edad <= 50:
    print("Es un adulto")
else:
    print("Es un adulto mayor")
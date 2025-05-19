placa1 = input("Ingrese la placa del bus 1: ")
pasajeros1 = int(input("Ingrese el número de pasajeros transportados por el bus 1: "))
valor_pasaje1 = float(input("Ingrese el valor del pasaje del bus 1: "))

dinero1 = pasajeros1 * valor_pasaje1

print()  # Línea en blanco para legibilidad
placa2 = input("Ingrese la placa del bus 2: ")
pasajeros2 = int(input("Ingrese el número de pasajeros transportados por el bus 2: "))
valor_pasaje2 = float(input("Ingrese el valor del pasaje del bus 2: "))

dinero2 = pasajeros2 * valor_pasaje2

if dinero1 > dinero2:
    print(f"\nEl bus que más dinero recogió fue el de placa {placa1} con ${dinero1:.2f}")
elif dinero2 > dinero1:
    print(f"\nEl bus que más dinero recogió fue el de placa {placa2} con ${dinero2:.2f}")
else:
    print(f"\nAmbos buses recogieron la misma cantidad de dinero: ${dinero1:.2f}")

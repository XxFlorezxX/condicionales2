placa = input("Ingrese la placa del bus: ")
pasajeros = int(input("Ingrese el número de pasajeros transportados: "))
ruta = input("Ingrese la ruta donde prestó el servicio (A o B): ").upper()

if ruta == "A":
    valor_pasaje = 1200
elif ruta == "B":
    valor_pasaje = 1000
else:
    print("Ruta inválida.")
    exit()

dinero_recolectado = pasajeros * valor_pasaje

print(f"\nEl bus con placa {placa} recolectó ${dinero_recolectado} en la ruta {ruta}.")

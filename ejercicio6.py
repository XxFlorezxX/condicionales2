tipo = input("Ingrese el tipo de trabajador (FIJO o TEMPORAL): ").upper()

if tipo == "FIJO":
    nombre = input("Ingrese el nombre del trabajador: ")
    horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
    salario_hora = float(input("Ingrese el salario básico por hora: "))
    deducciones = float(input("Ingrese el total de deducciones: "))
    bonificaciones = float(input("Ingrese el total de bonificaciones: "))

    salario_bruto = horas_trabajadas * salario_hora
    salario_neto = salario_bruto - deducciones + bonificaciones

elif tipo == "TEMPORAL":
    nombre = input("Ingrese el nombre del trabajador: ")
    horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
    salario_hora = 6000
    salario_neto = horas_trabajadas * salario_hora

else:
    print("Tipo de trabajador no válido.")
    exit()

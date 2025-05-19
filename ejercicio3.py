nombre1 = input("Ingrese el nombre del trabajador 1: ")
salario_bruto1 = float(input("Ingrese el salario bruto del trabajador 1: "))
deducciones1 = float(input("Ingrese las deducciones del trabajador 1: "))
bonificaciones1 = float(input("Ingrese las bonificaciones del trabajador 1: "))

salario_neto1 = salario_bruto1 - deducciones1 + bonificaciones1

nombre2 = input("\nIngrese el nombre del trabajador 2: ")
salario_bruto2 = float(input("Ingrese el salario bruto del trabajador 2: "))
deducciones2 = float(input("Ingrese las deducciones del trabajador 2: "))
bonificaciones2 = float(input("Ingrese las bonificaciones del trabajador 2: "))

salario_neto2 = salario_bruto2 - deducciones2 + bonificaciones2

if salario_neto1 > salario_neto2:
    print(f"\nEl trabajador con mayor salario neto es {nombre1} con {salario_neto1}")
elif salario_neto2 > salario_neto1:
    print(f"\nEl trabajador con mayor salario neto es {nombre2} con {salario_neto2}")
else:
    print(f"\nAmbos trabajadores tienen el mismo salario neto: {salario_neto1}")
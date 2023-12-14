# Calculadora de comisiones

nombre = input("Por favor, introduce tu nombre: ")
ventas = int(input("introduce tus ventas totales del mes: "))

comision = round(ventas * 13 / 100, 2)

print(f"{nombre}, tus comisiones de este mes son de ${comision}")

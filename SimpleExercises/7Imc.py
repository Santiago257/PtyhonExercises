#Ask
kg = float(input("Ingresa tu peso en kilo: "))
m = float(input("Ingresa tu tamaño en metros: "))

resultado = kg / (m ** 2)

print("Tu IMC es de: ", round(resultado,2))
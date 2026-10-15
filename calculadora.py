try:
    primer_numero = float(input("Ingresa el primer número: "))
    operador = input("Ingresa una operación (+, -, *, /): ")
    segundo_numero = float(input("Ingresa el segundo número: "))

    if operador == "+":
        resultado = primer_numero + segundo_numero
    elif operador == "-":
        resultado = primer_numero - segundo_numero
    elif operador == "*":
        resultado = primer_numero * segundo_numero
    elif operador == "/":
        if segundo_numero == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            resultado = primer_numero / segundo_numero
    else:
        print("Error: operación no válida.")

    if operador in ("+", "-", "*") or (operador == "/" and segundo_numero != 0):
        print(f"Resultado: {resultado}")
except ValueError:
    print("Error: ingresa números válidos.")

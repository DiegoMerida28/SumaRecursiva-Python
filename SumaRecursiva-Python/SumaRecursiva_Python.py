def suma_recursiva(n):
    # Caso base: cuando n es igual a 0, la suma es 0.
    if n == 0:
        return 0
    # Caso recursivo: suma n y el resultado de la suma recursiva de n-1.
    else:
        return n + suma_recursiva(n - 1)

# Solicitar al usuario que ingrese un n�mero entero positivo
numero = int(input("Ingresa un n�mero entero positivo: "))

if numero < 0:
    print("El n�mero debe ser positivo.")
else:
    resultado = suma_recursiva(numero)
    print(f"La suma de los n�meros enteros del 1 al {numero} es: {resultado}")


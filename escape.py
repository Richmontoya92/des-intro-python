import math as m

# Calculadora velocidad de escape

## Formula
### V = √(2gr)     g= constante gravitacional [m/s2]   r= radio del planeta en [m]

radio = float(input("Ingrese el radio en Kilómetros: "))
constante = float(input("Ingrese la constante g: "))

velocidad = m.sqrt(2 * constante * (radio * 1000))

print(f"La velocidad de Escape es: {velocidad:.2f} [m/s]")


# Razón Utilidades Actuales

## Fórmula: Utilidades actuales ( P x U - GT ) / Utilidades anterior 
### Variables: P = Precio de Suscripción ; U = Número de usuarios ; GT = Gastos Totales

precio_suscripcion = int(input("Ingrese precio de suscripción (número entero): "))
numero_usuarios = int(input("Ingrese el numero de usuarios: "))
gasto_total = int(input("ingrese gasto total (número entero): "))
utilidades_anterior = int(input("Ingrese utilidades del año anterior (número entero): "))

utilidades = ( precio_suscripcion * numero_usuarios ) - gasto_total

razon = utilidades / utilidades_anterior

print(f"La utilidad de este año es: {utilidades}")
print(f"La razón de utilidades es: {razon:.2f}")
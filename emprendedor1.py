

# Rentabilidad

## Fórmula: Utilidades = P x U - GT 
### Variables: P = Precio de Suscripción ; U = Número de usuarios ; GT = Gastos Totales

precio_suscripcion = int(input("Ingrese precio de suscripción (número entero): "))
numero_usuarios = int(input("Ingrese el numero de usuarios: "))
gasto_total = int(input("ingrese gasto total (número entero): "))

utilidades = ( precio_suscripcion * numero_usuarios ) - gasto_total

print(f"La utilidad total es: {utilidades}")
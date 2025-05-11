

# Rentabilidad

## Fórmula: Utilidades = ((P x U1) + (1.5x(PxU2)) - GT 
### Variables: P = Precio de Suscripción ; U = Número de usuarios ; GT = Gastos Totales

precio_suscripcion = int(input("Ingrese precio de suscripción (número entero): "))
numero_usuarios1 = int(input("Ingrese el numero de usuarios normales: "))
numero_usuarios2 = int(input("Ingrese el numero de usuarios premium: "))
gasto_total = int(input("ingrese gasto total (número entero): "))

utilidades = (( precio_suscripcion * numero_usuarios1 ) + (1.5*( precio_suscripcion * numero_usuarios2 ))) - gasto_total

print(f"La utilidad total es: {utilidades}")
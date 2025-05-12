def calcular_gasto_promedio(total_gastado, numero_dias):
    return total_gastado / numero_dias
def calcular_balance(presupuesto, gasto_promedio):
    return presupuesto / gasto_promedio
presupuesto = float(input("ingrese el presupuesto total del viaje: "))
numero_dias = float(input("Ingrese el numero de dias: "))
total_gastado = int(input("ingrese la cantidadad gastada hasta ahora: "))

gasto_promedio = calcular_gasto_promedio(total_gastado, numero_dias)
balance_diario = calcular_balance(presupuesto / numero_dias , gasto_promedio)
print(f"Gasto promedio diario${gasto_promedio}")
print(f"Balance disponible por dia{balance_diario}")
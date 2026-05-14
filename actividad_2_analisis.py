#creacion de litas de temperatura

# 1. Lista de temperaturas
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# 2. Indexación (Positivos y Negativos)
print(f"Primer día: {temperaturas[0]} | {temperaturas[-14]}")
print(f"Último día: {temperaturas[13]} | {temperaturas[-1]}")
print(f"Día 7 (mitad): {temperaturas[6]} | {temperaturas[-8]}")
print(f"Penúltimo día: {temperaturas[12]} | {temperaturas[-2]}")

# 3. Slicing
semana1 = temperaturas[0:7]
semana2 = temperaturas[7:14]
dias_pares = temperaturas[1::2] # Índices pares (2, 4, 6...) son posiciones impares en la lista
invertida = temperaturas[::-1]

print("\nSemana 1:", semana1)
print("Semana 2:", semana2)
print("Días pares de la quincena:", dias_pares)
print("Lista invertida:", invertida)

# 4. Cálculo de promedios
promedio_s1 = sum(semana1) / len(semana1)
promedio_s2 = sum(semana2) / len(semana2)

print(f"\nPromedio Semana 1: {promedio_s1:.2f}°C")
print(f"Promedio Semana 2: {promedio_s2:.2f}°C")

# 5. Bonus: Comparación
if promedio_s1 > promedio_s2:
    print("La primera semana tuvo la mayor temperatura promedio.")
elif promedio_s2 > promedio_s1:
    print("La segunda semana tuvo la mayor temperatura promedio.")
else:
    print("Ambas semanas tuvieron el mismo promedio.")
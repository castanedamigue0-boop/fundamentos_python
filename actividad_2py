# ==========================================
# Sistema de Gestión de Calificaciones
# ==========================================

# --- 1. Entrada de datos ---
# Solicitamos las notas y las convertimos a float para permitir decimales
nota1 = float(input("Ingrese la calificación parcial_1: "))
nota2 = float(input("Ingrese la calificación parcial_2: "))
nota3 = float(input("Ingrese la calificación parcial_3: "))

# --- 2. Validación y Cálculos ---
# Verificamos que ninguna nota supere el máximo permitido (5.0)
if nota1 <= 5 and nota2 <= 5 and nota3 <= 5:
    
    # Calculamos el promedio aritmético simple
    promedio = (nota1 + nota2 + nota3) / 3

    # Calculamos la diferencia respecto a la nota máxima
    puntos_faltantes = 5.0 - promedio 

    # Determinamos si el estudiante aprueba (mínimo 3.0)
    # Esto guarda un valor booleano (True o False)
    aprobado = promedio >= 3.0

    # --- 3. Salida de resultados ---
    print("\n" + "="*30)
    print(f"El promedio final es: {round(promedio, 2)}")
    print(f"Puntos para la nota máxima (5.0): {round(puntos_faltantes, 2)}")

    # Estructura condicional para mostrar el estado final
    if aprobado:
        print("Estado: ✅ APROBADO")
    else:
        print("Estado: ❌ REPROBADO")
    print("="*30)

else:
    # Mensaje de error si alguna nota es inválida (mayor a 5.0)
    print("\n⚠️ ERROR: Las calificaciones no pueden ser mayores a 5.0")
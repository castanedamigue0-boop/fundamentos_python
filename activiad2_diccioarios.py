#=================================================
#sisema de regitro e prendices
#=================================================

# ==========================================
# Actividad: Sistema de Registro de Aprendices
# ==========================================

# --- PASO 2: Función para calcular el promedio ---
def calcular_promedio(lista_notas):
    """Recibe una lista de notas y retorna el promedio."""
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)


# --- PASO 1: Creación del diccionario 'grupo' (Mínimo 4 aprendices) ---
grupo = {
    101: {
        "nombre": "Ana Gomez",
        "edad": 21,
        "notas": [4.5, 3.8, 4.2, 4.0],
        "ciudad": "Bogotá"
    },
    102: {
        "nombre": "Juan Pérez",
        "edad": 19,
        "notas": [2.5, 3.0, 2.8, 3.2],
        "ciudad": "Medellín"
    },
    103: {
        "nombre": "María Rojas",
        "edad": 24,
        "notas": [4.8, 4.9, 4.7, 5.0],
        "ciudad": "Cali"
    },
    104: {
        "nombre": "Luis Torres",
        "edad": 22,
        "notas": [2.0, 3.5, 2.2, 3.0],
        "ciudad": "Bucaramanga"
    }
}


# --- PASO 4: Agregar un nuevo aprendiz y actualizar una ciudad ---
# Agregar nuevo aprendiz
grupo[105] = {
    "nombre": "Carlos Mendoza",
    "edad": 20,
    "notas": [3.5, 4.0, 3.8, 4.1],
    "ciudad": "Cartagena"
}

# Actualizar la ciudad de uno de los aprendices existentes (ej. el de ficha 102)
grupo[102]['ciudad'] = 'Manizales'


# --- PASO 3: Imprimir reporte usando .items() y ciclo for ---
print("-" * 70)
print(f"{'FICHA':<8} | {'NOMBRE':<15} | {'EDAD':<4} | {'PROMEDIO':<8} | {'ESTADO':<10}")
print("-" * 70)

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])
    
    # Determinar el estado (APROBADO si promedio >= 3.0)
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    
    print(f"{ficha:<8} | {datos['nombre']:<15} | {datos['edad']:<4} | {promedio:<8.2f} | {estado:<10}")

print("-" * 70)
print("\n")


# --- PASO 5 (BONUS): Ordenar de mayor a menor promedio con sorted() ---
print("=" * 45)
print("  REPORTE ORDENADO POR PROMEDIO (MAYOR A MENOR)  ")
print("=" * 45)

# Ordenamos los items del grupo. La clave de ordenación (key) calcula el promedio de cada aprendiz.
# reverse=True asegura que vaya de mayor a menor.
grupo_ordenado = sorted(
    grupo.items(), 
    key=lambda item: calcular_promedio(item[1]["notas"]), 
    reverse=True
)

for ficha, datos in grupo_ordenado:
    promedio = calcular_promedio(datos["notas"])
    print(f"Ficha: {ficha} | Nombre: {datos['nombre']:<15} | Promedio: {promedio:.2f}")

print("=" * 45)
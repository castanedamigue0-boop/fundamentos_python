#===============================================
#Análisis de Matrículas del Centro de Formación
#===============================================

# ---- paso 1: definicion de los conjuntod de apremdices ----
python_curso ={"ana","martha","carlos","sofia","pedro"}
java_curso ={"luis","carlos","pedro","laura","diego"}
bd_curso ={"marths","sofia","laura","ana","miguel"}

# ---- paso 2: operaciones conjuntos ----
print("----operacines de conjuntos----")

#A.  Total de aprendices únicos en los tres programas
todos_los_aprendices = python_curso.union(java_curso).union(bd_curso)
print(f"!: Total de aprendices unicoS:{len(todos_los_aprendices)}")
print(f"    lista completa:{todos_los_aprendices}\n")

#B. Aprendices que cursan Python Y Java simultáneamente
python_y_java =python_curso.difference(java_curso)
print(f"2. aprendices en python y java:{python_y_java}\n")

# C. Aprendices que SOLO están en Python
solo_python = python_curso.difference(java_curso).difference(bd_curso)
print(f"3. aprendices solo python:{solo_python}\n")

# D. Aprendices en EXACTAMENTE dos programas (ni uno solo, ni en los tres)
# Lógica: (Py y Ja) + (Py y BD) + (Ja y BD) menos 3 veces la intersección triple
interseccion_triple = python_curso.intersection(java_curso).intersection(bd_curso)
en_dos_programas = (
    (python_curso & java_curso) |
    (python_curso & bd_curso)   |
    (java_curso & bd_curso) 
) - interseccion_triple

print(f"4. aprendices en exactamente dos programas: {en_dos_programas}\n")

# --- PASO 3: Filtrar duplicados de una lista usando un conjunto ---
print("-" * 60)
print("--- CONTEO DE INSCRIPCIONES ÚNICAS (PASO 3) ---")
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']

# Al transformar la lista a un set, se eliminan los duplicados automáticamente
aprendices_unicos_inscritos = set(inscripciones)

print(f"Cantidad de inscritos únicos: {len(aprendices_unicos_inscritos)}")
print(f"¿Quiénes son?: {aprendices_unicos_inscritos}\n")


# --- PASO 4: Diccionario por comprensión conteo_programas ---
print("-" * 60)
print("--- CONTEO DE PROGRAMAS POR APRENDIZ (PASO 4) ---")

# Generamos una lista auxiliar combinando todos los cursos para contar las apariciones
todas_las_matriculas = list(python_curso) + list(java_curso) + list(bd_curso)

conteo_programas = {
    aprendiz: todas_las_matriculas.count(aprendiz) 
    for aprendiz in todos_los_aprendices
}

print("Diccionario conteo_programas:")
for nombre, cantidad in conteo_programas.items():
    print(f"  - {nombre}: {cantidad} curso(s)")
print()


# --- PASO 5 (BONUS): Aprendices matriculados en los tres programas ---
print("-" * 60)
print("--- BONUS (PASO 5) ---")
print(f"Aprendices matriculados en los tres programas a la vez: {interseccion_triple}")
print("-" * 60)
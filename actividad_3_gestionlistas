# 1. Declarar lista inicial con 5 canciones colombianas
canciones = ["La Camisa Negra", "Cali Pachanguero", "La Gota Fría", "Robarte un Beso", "Colombia Tierra Querida"]

# 2. Aplicar métodos en orden
canciones.append("Provenza") # Agrego una nueva al final (Karol G)
canciones.insert(1, "Hips Don't Lie") # Inserto en la segunda posición (Shakira)
# Fusiono la lista con los bonus tracks que pide la guía
canciones.extend(["Bonus Track 1", "Bonus Track 2"]) 

print("Estado de la lista tras modificaciones:", canciones)

# 3. Eliminar elementos
# Elimino una por nombre (Cali Pachanguero)
canciones.remove("Cali Pachanguero") 
# Elimino la última de la lista y guardo su valor
eliminada = canciones.pop() 
print(f"Canción eliminada con pop(): {eliminada}")

# 4. Ordenar alfabéticamente
canciones.sort()
print("Lista ordenada alfabéticamente:", canciones)

# 5. Respuestas a preguntas usando métodos
print(f"\n¿Cuántas canciones tiene la playlist?: {len(canciones)}")
# Busco la posición de la primera canción que agregué con append ('Provenza')
print(f"¿En qué posición está 'Provenza'?: {canciones.index('Provenza')}")
print(f"¿Cuántas veces aparece 'Bonus Track 1'?: {canciones.count('Bonus Track 1')}")
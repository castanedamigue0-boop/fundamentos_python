# 1. Importamos la librería para que la computadora elija al azar
import random 

# 2. Mostramos un mensaje estético de inicio usando la función print()
print("=== BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA ===")

# 3. Pedimos al usuario su jugada con input() y la pasamos a minúsculas
usuario = input("Escribe tu jugada (piedra/papel/tijeras): ").lower()

# 4. Definimos una lista de opciones para que la PC pueda elegir una
opciones = ["piedra", "papel", "tijeras"]

# 5. La computadora elige una opción al azar de la lista usando random
computadora = random.choice(opciones)

# 6. Imprimimos un separador visual para la consola
print("----------------------------------------------------")

# 7. Mostramos qué eligió el jugador usando un f-string
print(f"Elegiste: {usuario}")

# 8. Mostramos qué eligió la máquina para que el usuario compare
print(f"La computadora eligió: {computadora}")

# 9. Primer nivel de lógica: Usamos IF para detectar si hubo un empate
if usuario == computadora:
    # 10. Si el operador '==' es verdadero, se imprime este mensaje
    print("¡Es un empate técnico! 🤝")

# 11. Segundo nivel: Usamos ELIF si el usuario eligió 'piedra'
elif usuario == "piedra":
    # 12. IF anidado: Si el usuario tiene piedra, revisamos si PC tiene tijeras
    if computadora == "tijeras":
        # 13. Mensaje de victoria si la condición de arriba se cumple
        print("¡Ganaste! La piedra rompe las tijeras. 🏆")
    # 14. ELSE: Si no es empate ni tijeras, por lógica la PC tiene papel
    else:
        # 15. Mensaje de derrota si la PC tiene papel
        print("Perdiste... El papel envuelve la piedra. ❌")

# 16. Tercer nivel: Evaluamos el escenario si el usuario eligió 'papel'
elif usuario == "papel":
    # 17. Revisamos la condición de victoria para el papel (contra piedra)
    if computadora == "piedra":
        # 18. Resultado ganador para papel
        print("¡Ganaste! El papel envuelve la piedra. 🏆")
    # 19. Si la PC no tiene piedra, entonces tiene tijeras
    else:
        # 20. Resultado perdedor para papel
        print("Perdiste... Las tijeras cortan el papel. ❌")

# 21. Cuarto nivel: Evaluamos el escenario si el usuario eligió 'tijeras'
elif usuario == "tijeras":
    # 22. Condición de victoria: tijeras vencen a papel
    if computadora == "papel":
        # 23. Mensaje que confirma que el usuario ganó
        print("¡Ganaste! Las tijeras cortan el papel. 🏆")
    # 24. Si la PC no tiene papel, significa que tiene piedra
    else:
        # 25. Mensaje que confirma que la PC ganó
        print("Perdiste... La piedra rompe las tijeras. ❌")

# 26. Quinto nivel: ELSE final por si el usuario escribió algo incorrecto
else:
    # 27. Aviso de error para entradas no válidas (ej: 'hola' o '123')
    print("Error: Debes escribir 'piedra', 'papel' o 'tijeras'.")

# 28. Cierre decorativo final para concluir la ejecución del programa
print("================ GAME OVER ================")
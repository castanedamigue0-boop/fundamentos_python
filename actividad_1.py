# ==========================================
# Actividad 1 - Fundamentos de Python
# ==========================================

# PUNTO 2: Definición de Variables y Tipos de Datos
# Aquí se almacenan diferentes tipos de información: strings (texto), 
# integers (enteros), floats (decimales) y booleans (lógicos).
nombre = "miguel "               # String (str)
apellido = "castañeda"           # String (str)
edad = 18                        # Integer (int)
altura = 1.75                    # Float (float)
activo = True                    # Boolean (bool)
correo = "castanedamigue0@gmail.com"
telefono = "3106192145"          # String (aunque sean números, se trata como texto)
cedula = 1088830154              # Integer (int)
ficha = "321349"                 # String (str)
programa = "ADSO"                # String (str)

# PUNTO 3: Verificación de Tipos de Datos
# Usamos la función type() para identificar la clase de cada variable
# y print() para mostrar el resultado en la consola.
print("--- Verificación de Tipos ---")
print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(cedula), cedula)
print(type(ficha), ficha)
print(type(programa), programa)

# PUNTO 4: Conversión de Tipos de Datos (Casting)
# Transformamos las variables originales a nuevos tipos según lo requerido.
print("\n--- Resultados de las Conversiones ---")

# Convertir teléfono (string) a entero (int)
telefono_int = int(telefono)
print(f"Teléfono a int: {type(telefono_int)}")

# Convertir edad (entero) a decimal (float)
edad_float = float(edad)
print(f"Edad a float: {type(edad_float)} -> {edad_float}")

# Convertir altura (decimal) a entero (int)
# Nota: Al convertir a int, Python trunca los decimales (no redondea).
altura_int = int(altura)
print(f"Altura a int: {type(altura_int)} -> {altura_int}")

# Convertir cédula (entero) a cadena de texto (string)
cedula_str = str(cedula)
print(f"Cédula a string: {type(cedula_str)} -> '{cedula_str}'")
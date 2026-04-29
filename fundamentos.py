print("hello world")

# tipo de estructura de datos

camelCase = "sena"  # la primera letra de cada palabra va en mayuscula excepto la primera palabra
snake_case = (
    "sena"  # todas las letras van en minuscula y las palabras se separan por guion bajo
)
PascalCase = "Sena"  # la primera letra de cada palabra va en mayuscula
aprendiz_sena = (
    "sena"  # todas las letras van en minuscula y las palabras se separan por guion bajo
)

_aprendiz = "sena"  # todas las letras van en minuscula y las palabras se separan por guion bajo, ademas de que el nombre de la variable empieza con un guion bajo
x = "esta es una x minuscula"  # todas las letras van en minuscula y las palabras se separan por guion bajo, ademas de que el nombre de la variable es una sola letra
print(
    x
)  # todas las letras van en minuscula y las palabras se separan por guion bajo, ademas de que el nombre de la variable es una sola letra

X = "esta es una X mayuscula"  # todas las letras van en minuscula y las palabras se separan por guion bajo, ademas de que el nombre de la variable es una sola letra pero esta letra es mayuscula
print(
    X
)  # todas las letras van en minuscula y las palabras se separan por guion bajo, ademas de que el nombre de la variable es una sola letra pero esta letra es mayuscula

# tipos de datos
nombre = "miguel "
apellido = "castañeda"
edad = 18
altura = 1.75
activo = True
correo = "castanedamigue0@gmail.com"
telefono = "3106192145"
cedula = 1088830154

# imprimir el tipo de dato de cada variable
print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono))
print(type(cedula), cedula)

# convertir el tipo de dato de telefono a entero, edad a float, altura a entero y cedula a string
telefono_int = int(telefono)
print(type(telefono_int))
edad_float = float(edad)
altura_int = int(altura)
cedula_str = str(cedula)
print(type(altura_int), altura_int)
print(type(edad_float), edad_float)
print(type(cedula_str), cedula_str)

# identacion
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

nombre_completo =  input("ingresa tu nombre completo: ")
print("hello: " + nombre_completo)


edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("eres mayor de edad")
else:    
    print("eres menor de edad")

# concatenacion de cadenas de texto e interpolacion de cadenas de texto


print ("hola " + nombre_completo + " tu edad es: " + str(edad))# concatenacion de cadenas de texto, se convierte la variable edad a string para poder concatenarla con el resto de la cadena de texto
print(f"hola {nombre_completo} tu edad es: {edad}")# interpolacion de cadenas de texto, se utiliza la letra f antes de las comillas para indicar que se va a utilizar la interpolacion, y se utilizan las llaves para indicar las variables que se van a interpolar


#operadores arimeticos
a = 10 
b = 5 

suma = a + b
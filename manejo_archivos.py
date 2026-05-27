#open(nombre, modo) -> funciones de python para manipilar archivos

#R (read) lectura
#W (write) escritura
#X (crear archibo nuevo)

try:
    file = open("archivo.txt", "r")
    print(file.readline()) #lee la primera linea
    file.close()
except FileNotFoundError:
    print("no se encontro el archivo")
    
#uso de WITH para cerrar el archivo manualmente
try:
    with open("archivo.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("no se encontro el archivo")
    

#sobreesbir un archivo en el sistema
try:
    with open("archivo.txt", "w") as file:
        file.write("texto sobrescrito")#sobrescribe
except FileNotFoundError:
    print("no se encontro el archivo")
    
try:
    with open("archivo.txt", "a") as file:
        print(file.readline)
except FileNotFoundError:
    open("archivo.txt", "x")
    print("no se encontro el archivo")
    
def crear_archivo_html(script_archivo):
    try: 
        with open(script_archivo, "w") as file:
            print(file.read())
    except FileNotFoundError:
        open("pepe.html", "x")
        print("no se encontro el archivo")
    
try:
    with open("pepito.html", "w") as file:
        file.write("script_html")
        with open("pepito.html", "r") as file:
            print(file.read())
except FileNotFoundError:
    print("no se encontro el archivo")
    
crear_archivo_html("pepito.html").


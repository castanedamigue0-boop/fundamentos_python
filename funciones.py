#FUNCION: bloque de codigo reutilizable que realiza una tarea especifica.

#definir una funcion 

def nombre_funcion():
    print("hola,soy una funcion")
    
#llamar a la funcion 
nombre_funcion()

#funcion con parametro

def saludar(nombre):
    return f"hola, {nombre}, bienvenido a la progracion con funciones" 

print(saludar("felipe"))
print(saludar("miguel"))


#operaciones matematicas con funciones

#funcion para sumar
def sumar(num_1, num_2):
    sumar = num_1 + num_2
    return sumar
print(sumar(3, 2))

#funcion para restar

def resta(num_1,num_2):
    resta = num_1 - num_2
    return resta

print(resta(110, 5))

#Funcion para multiplicar
def multiplicacion(num_1, num_2):
    multiplicacion = num_1 * num_2
    return multiplicacion

print(multiplicacion(4,8))

#Funcion para dividir

def division(num_1, num_2):
    division = num_1 / num_2
    return division

print(division(45,5))

#Ejercicio para clasificar edad

def  clasificar_edad(edad):
    if edad < 18:
        if edad > 12 and edad < 18:
            print("Adolecente")
        else:
            print("Niño")
    
    else:
        if edad >= 18 and edad < 60:
            print("Eres un adulto")
        else:
            print("eres un adulto mayor")
    
  # edad = int(input("Ingrese su edad:"))
clasificar_edad(15)


#Usuarios sofia plus SENA
aprendices_ficha_3321349 = ["Felipe", "Andres", "Sofia", "Camilo", "Valentina", "Daniela", "Sebastian", "Maria"]
aprendices_ficha_2231229 = ["Felipe", "Juan", "Pedro", "Ana", "Lucia", "Miguel", "Elena", "Diego", "Isabella"]

#funcion para mostrar los aprendices de la ficha

def mostrar_aprendices(ficha):
    print(f"los apreneices de la ficha {ficha} son:")
    for aprendiz in ficha:
        print(aprendiz)
    
mostrar_aprendices(aprendices_ficha_3321349)
mostrar_aprendices(aprendices_ficha_2231229)

#Funcion para agregar u nuevo aprendiz a la ficha

def agregar_aprendiz(ficha, aprendiz):
    ficha.append(aprendiz)
    print(f"El aprendiz {aprendiz} ha sido agregado a la ficha")

agregar_aprendiz(aprendices_ficha_3321349, "Brayan")


#funcion para modificar el nombre de un aprendiz

def modificar_aprendiz(ficha, aprendiz_viejo, aprendiz_nuevo):
    if aprendiz_viejo in ficha: #BUSQUEDA TRUE
        indice = ficha.index(aprendiz_viejo)    #Busqueda del Elemento en la Lista por el nombre para saber el Indice
        ficha[indice] = aprendiz_nuevo
        print(f"el nombre del aprendiz a sido modificado a {aprendiz_nuevo}")
    else:
        print(f"el aprendiz {aprendiz_viejo} no se encuentra en la ficha")
    
modificar_aprendiz(aprendices_ficha_3321349, "Felipe", "Vegeta")
mostrar_aprendices(aprendices_ficha_3321349)


#Eliminar un aprendi de la ficha

def eliminar_aprendiz(ficha, aprendiz_borrado):
    if aprendiz_borrado in ficha:
        ficha.remove(aprendiz_borrado)
        print(f"el aprendiz borrado {aprendiz_borrado} ha sido eliminado de la ficha {ficha}")
    else:
        print(f"el aprendiz borrado {aprendiz_borrado} no se encuentra en la ficha {ficha}")
    
eliminar_aprendiz(aprendices_ficha_3321349, "Vegeta")

mostrar_aprendices(aprendices_ficha_3321349)
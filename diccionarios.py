#diccionaros (caracteristicas)

#creacion de un diccionario

#estructura de un diccionario
from turtle import update


diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}

#diccionario bacio
diccionario_vacio={}

#dicconario con elementos
diccionario_aprendiz={
    "nombre":"felipe",
    "apelllido":"sandoval",
    "programa":"ADSO",
    "ficha":"3321349",
    "edad":32
}

print(type(diccionario_aprendiz)) #class <dict>

#obtener un valor del diccionario
print(diccionario_aprendiz["programa"])
print(diccionario_aprendiz.get("programa"))

#obtener solo las claves del diccionario
print(diccionario_aprendiz.keys())

#obtenerolo los valores del diccionario
print(diccionario_aprendiz.values())

#obtener la clave y el valor
print(diccionario_aprendiz.items())

#agregar un nuevo elemento al diccionario 
diccionario_aprendiz["correo"]= "castanedamigue0@gmail.com"

#modificar un valor del diccionario
diccionario_aprendiz["programa"]= "SST"
print(diccionario_aprendiz)

#metodoUPDAET()
diccionario_aprendiz.update({"nombre":"andres"})
diccionario_aprendiz.update({"ciudad":"duitama"})
print(diccionario_aprendiz)

#comprobar pertenencia (In)
if "ficha" in diccionario_aprendiz:
    print("ficha es una de las propiedades de este diccioanario")

#recorer un diccionario con un ciclo for

#reorrer slolas claves del diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)

#recorrer solo los valores del diccionario 
for valor in diccionario_aprendiz.values():
    print(valor)

#recorrer las claves y los valore del diccionario
for clave, valor in diccionario_aprendiz.items():
    print(f"{clave}:{valor}")

#eliminar elementos en un diccionario POP()
diccionario_aprendiz.popitem()
print(diccionario_aprendiz)

diccionario_aprendiz.pop("edad")
print(diccionario_aprendiz)

diccionario_aprendiz.clear() # Elimina todo el diccionario
print(diccionario_aprendiz)

# diccionarios anidados
aprendices = {
    "aprendiz_1": {
        "nombre": "felipe",
        "apelllido": "sandoval",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 32
    },
    "aprendiz_2": {
        "nombre": "andres",
        "apelllido": "sandoval",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 32
    },

        "aprendiz_3": {
        "nombre": "andres",
        "apelllido": "sandoval",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 32
    }
}


# acceder a un diccionario anidado

print(aprendices["aprendiz_2"]["programa"]) #SST
for aprendiz, datos in aprendices.items ():
    print(f"{aprendiz}:")
    for clave, valor in datos.items():
        print(f"{clave}, {valor}")



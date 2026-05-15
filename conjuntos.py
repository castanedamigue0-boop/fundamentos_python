# Conjuntos ((SETS) en phyton)

# structura de un conjunto

conujunto = set()

print(type(conujunto))

lenguajes = ("python", "java", "c++")

# metodos de modificacion

frutas = {"mango", "guayaba", "mora"}
frutas.add("maracuya") # agraga un elemnto
frutas.add("mango") # no lo agrega porque ya existe
frutas.remove("maracuya") #quita un elemento
frutas.discard("mango") #elimina NO lanza error si no existe
elem = frutas.pop() #elimina y retorna un elemnto aleatorio
print(elem)


# verificar pertenencia

print("Phyton" in lenguajes)
print("COBOL" in lenguajes)

python_devs = {"Ana", "Luis", "Marta", "Carlos", "Sofía"}
java_devs   = {"Luis", "Carlos", "Pedro", "Laura"}

# ┌──────────────────────────────────────────────────────┐
# │ UNIÓN | : todos los elementos de ambos conjuntos    │
# └──────────────────────────────────────────────────────┘

todos = python_devs | java_devs
# o también: python_devs.union(java_devs)

print("Unión:", todos)

# {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofía', 'Pedro', 'Laura'}

# ┌──────────────────────────────────────────────────────┐
# │ INTERSECCIÓN & : solo los que están en AMBOS        │
# └──────────────────────────────────────────────────────┘

ambos = python_devs & java_devs
# o también: python_devs.intersection(java_devs)

print("Intersección:", ambos)   # {'Luis', 'Carlos'}

# ┌──────────────────────────────────────────────────────┐
# │ DIFERENCIA - : los de A que NO están en B           │
# └──────────────────────────────────────────────────────┘

solo_python = python_devs - java_devs
# o también: python_devs.difference(java_devs)

print("Solo Python:", solo_python)
# {'Ana', 'Marta', 'Sofía'}

solo_java = java_devs - python_devs
print("Solo Java:", solo_java)
# {'Pedro', 'Laura'}

# ┌─────────────────────────────────────────────────────────────┐
# │ DIFERENCIA SIMÉTRICA ^ : los que están en uno PERO no en ambos │
# └─────────────────────────────────────────────────────────────┘

exclusivos = python_devs ^ java_devs

# o también: python_devs.symmetric_difference(java_devs)

print("Exclusivos:", exclusivos)

# {'Ana', 'Marta', 'Sofía', 'Pedro', 'Laura'}
#TUPLAS

#estrucutura de una tupla

from ast import AugStore


tupla =("elemento_1","elemento_2","elemento_3")
print(type(tupla)) #<class "tuple">

tupla = "a", "b" "c"
print(type(tupla))

tupla_4 = tuple ("hola")
print(tupla_4) 

#trupla aprendices sena adso

#indice
aprendices =("simon", "sharit", "caimlo", "miguel","daniela", "grisell")
print(aprendices)

#acceder a un elemento de la tupla
print(aprendices)

#consulta rangos de un elemento de la lista
print(aprendices [0:2]) # simo y sharit
print(aprendices [1:5]) #sharit camilo miguel daniela
print(aprendices [1:]) #sharit camilo miguel daniela gisell

#sumar 2 tuplas
tupla_1= (1, 2, 3)
tupla_2= (4, 5, 6)
tupla_suma = tupla_1 + tupla_2
print(tupla_suma)

#multiplicaciob ua tupla 
tupla_multiplicada = tupla_1 * 3
print(tupla_multiplicada)

#metodos de las tuplas

#medir el laro con len()
print(len(aprendices))

#conta elementos repetidos en una tupla con count
print(aprendices.count("grisell"))

#obtener el indice d eun elemento con index
print(aprendices.index("miguel"))


#modificar una tupla en una lista
print(type(aprendices))
aprendices_lista =list(aprendices)
print(type(aprendices_lista))
aprendices_lista.append("sara")
print(aprendices_lista)

aprendices = tuple(aprendices_lista)
print(aprendices)

programa_1 ="aADSO"
programa_2="SST"
programa_3="TOPOGRAFIA"
#desempaquetrar una dupla 
tupla_desempaquetada =("ADSO","SST","TOPOGRAFIA")
programa_1, programa_2, programa_3
print(programa_1)

#ejercicio 2 desquempaquetar
tupla_ciudades =("bogota", "medellin","cali")
ciudad_1, ciudad_2, ciudad_3 =tupla_ciudades
print(ciudad_1)
print(ciudad_2)
print(ciudad_3)

for ciudad in tupla_ciudades:
    print(ciudad)


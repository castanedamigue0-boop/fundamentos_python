#operadores aritmeticcos
a = 10
b = 5

#suma
suma = a + b
print(f"la suma de {a} y {b} es: {suma}")

#resta
resta = a - b
print(f"la resta de {a} y {b} es: {resta}")

#multiplicacion
multiplicacion = a * b
print(f"la multiplicacion de {a} y {b} es: {multiplicacion}")

#division flotante o decimal 
division = a / b
print(f"la division de {a} y {b} es: {division}")

#modulo
modulo = a % b
print(f"el modulo de {a} y {b} es: {modulo}")

#division entera
division_entera = a // b
print(f"la division entera de {a} y {b} es: {division_entera}")

#potencia
potencia = a ** b
print(f"la potencia de {a} y {b} es: {potencia}")

#procedencia de operadores

resultado_2 = a + b * 2
print(f"el resultado de la operacion es {a} + {b} * 2 es: {resultado_2}")

resultado_3 = a * b // 3
print (f"el resultado de la operavion es {a} + {b} // 3 es: {resultado_3}")

resultado_4 = (a * b) // 3
print (f"el resultado de la operracion es ({a} * {b}) // 3 es: {resultado_4}")

resultado_5 = a* (b // 3)
print (f"el resultado de la operacion es {a} * ({b} // 3) es: {resultado_5}  ")

ejercicio = ((a + b) * (a -b) / (a * b)) - ((a ** b) % 3)
print (f"el resultado de la operacio ({a} + {b}) * ({a} - {b}) / ({a} * {b}) es: {ejercicio}")

#librerias de matematicas 

import math
import random 

print (math.pi)
print (math.e)
print (math.sqrt(16))

import random

random.random ()
numero_aleatorio = random.randint (1, 10)
print (numero_aleatorio)
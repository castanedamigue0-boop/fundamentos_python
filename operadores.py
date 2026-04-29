#operadores arimeticos
valor_1 = int(input("ingresa un numero: "))
valor_2 = int(input("ingresa otro numero: "))

#operadores arimeticos
suma = valor_1 + valor_2
resta = valor_1 - valor_2
multiplicacion = valor_1 * valor_2
division = valor_1 / valor_2
modulo = valor_1 % valor_2
divicion_entera = valor_1 // valor_2
potencia = valor_1 ** valor_2

#operadores de asignacion
selector = input("ingresa el operador que deseas usar (+, -, *, /, %, //, **): ")
if selector == "+":
    print(f"la suma de {valor_1} y {valor_2} es: {suma}")
elif selector == "-":
    print(f"la resta de {valor_1} y {valor_2} es: {resta}")
elif selector == "*":
    print(f"la multiplicacion de {valor_1} y {valor_2} es: {multiplicacion}")
elif selector == "/":
    print(f"la division de {valor_1} y {valor_2} es: {division}")
elif selector == "%":
    print(f"el modulo de {valor_1} y {valor_2} es: {modulo}")
elif selector == "//":
    print(f"la division entera de {valor_1} y {valor_2} es: {divicion_entera}")
elif selector == "**":
    print(f"la potencia de {valor_1} y {valor_2} es: {potencia}")  
else:
    print("operador no valido")





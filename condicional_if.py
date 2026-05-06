#condicionales IF/ELIF/ELSE

if True:
    print("la condicion es verdadera")
elif False:
    print("ña segunda condicional es verdadera ELIF")
elif True:
    print("la terccera condiconal es verdadera  ELIF")
else:
    print("la condicional es falsa")


edad = 15

if edad <= 18:
    print("eres un adulto")
elif edad >= 18 and edad <65:
    print("eres un adulto")
else: 
    print("eres un menor de edad")

# ejercicio: clasificacon de edad F anidado 

edad = 70

if edad < 18:
    if edad > 12 and edad < 18:
        print("eress un adolecente")
else:
    print("eres un adulto")

edad = int(input("ingrese su edad para ser calificado: "))

if edad < 18:
    if edad > 12 and edad < 18:
        print("ADOLECENTE")
    else:
        print("NIÑO")
else:
    if edad >=18 and edad <60:
        print("eres un adulto")

    else:
        print("eres un adulto mayor")    


#operadores ternario 

numero =4
 
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

print("el numero es par" if numero %2 ==0 else "el numero es impar")
 
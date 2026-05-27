#manejo de errores: try-except

#estructure

try: 
    print("intentamos algo")
except:
    print("captura el error")
finally:
    print("esto sera ejecutado siendo exiroso o no en el bloque")

#ejemplo:covetir o castear datos de entrada del usuario

try:
    edad_usuario =int(input("ingrese su edad: "))
except:
    print("ingrese solo numeros")

#ejemplo: variable no definida
try:
    print(x)
except NameError:
    print("la variable no existe")
    
#EJEMPL0: divo por cero

try:
    print(10/0)
except ZeroDivisionError:
    print("ey pendejo no se puede dividir por cero")
    
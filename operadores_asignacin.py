#operadores de asigncion 

from re import X


x = 5
print(x)
x = x + 2 #suma y asignacon
x +=2
print (x)

x = x ** 2 #exponenciacion y asignacion
x **=2 
print (x)

x = 10 # asignacion la valeriable x a 10
print (x) #imprimir el valor x

# walrus operador (python 3.8+) :=
print (x := 10)
#operadores logicos permite construir expresiones logicas se obtiene como resultado booleanos
#And (conjugacion) amd  true tiene valor = 1 
#OR (disyuncion) or     false tiene valor = 0
#negacion not           orden de prioridad operadores logicos 1.- NOT 2.-AND 3.-OR

#operador AND
#true and true = true
#true and false = false
#false and true = false
#false and false = false
#operador OR
#true or true = true
#true or false = true
#true or true = true
#true or false = false 
#operador negacion
#not(True) = False
#not(False) = true

a =10   #ejercicio
b = 12 
c = 13 
d = 10;

resultado1 = a > b 
resultado2 = a < c
resultado3 = a == c 
resultado4 = a >=b 
print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4) 
resultadofinal = ((a>b)) or ((a<c)) and ((a==c)) or ((a>=c))
print(resultadofinal)

e = 10        #ejercicio
f = 15
g = 20 

resultado2 = ((e<f)) and ((f<g))
print(resultado2) 

#ejercicio 
#a == X
#resultado = (a**3 *(b**2 - 2ac)) /2b
#print(resultado)

#solucion
a =float(input("a ->"))
b =float(input("b ->"))
c =float(input("c ->"))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"el resultado es: {resultado}")
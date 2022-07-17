#https://github.com/yiaf/pythonbasico
#Ingresa tre numeros y determina
#cual es el mayor de los tres"
a = int(input("Ingresar primer número: "))
b = int(input("Ingresar segundo número: "))
c = int(input("Ingresar tercer número: "))
if a>b:
    mayor = a
else:
    mayor = b
if c > mayor:
    mayorahoraes = c
else:
    mayorahoraes = mayor

print("El número mayor es:", mayorahoraes )

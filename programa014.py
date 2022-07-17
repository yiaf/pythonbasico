#https://github.com/yiaf/pythonbasico
#Halla el nuemro de divisiones
x = int(input("Ingresa un numero: "))
n=0
e= x/2 
while e > 0.000000054321:
    n = n + 1
    e = x / (2**n)
    print(e)
print("El nùmero de divisiones es: ",n)
      
     


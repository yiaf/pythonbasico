#https://github.com/yiaf/pythonbasico
#Crea una lista numeros y recorre buscando el mayor
#Recuerde la posición incial de una lista es 0
listado = [90,100,50,60,70,37,25,1,0,200,201,90,99,701,100,101]
mayor = listado[0]
n = len(listado)
i=0
while i < n-1:
    i+=1
    if mayor < listado[i]:
        mayor = listado[i]
        pos= i
print("El mayor es: ",mayor, "En la posicion ",pos)  
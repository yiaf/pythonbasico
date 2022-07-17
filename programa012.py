#https://github.com/yiaf/pythonbasico
#Ingresar siempre un numero positivo"
numero = int(input("Ingresa un numero positivo: "))
while numero <= 0:
    print("Incorrecto...")
    numero = int(input("Ingresa un numero positivo: "))
print("ok... Nro positivo")



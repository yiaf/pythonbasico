#https://github.com/yiaf/pythonbasico
#Mientras controlado por evento
deuda = 0
valor = int(input("Presine la tecla 0,para salir: "))
while valor != 0:
    deuda = deuda + 1000
    print("Ahora su deuda es: ",deuda," Soles")
    valor = int(input("Presine la tecla 0,para salir: "))
print("Su deuda acumulada fue: ", deuda)
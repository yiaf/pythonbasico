#https://github.com/yiaf/pythonbasico
#Mientras - sino
#Un caso extraño, para desarrolladores en Java, c++
#Comenta la línea 12 con # y verifica los resultados
i = 1
print("Tiene 3 intentos")
while i <= 3:
    txt = input("Escribe PERÚ ")
    if txt == 'PERÚ':
        print("Lo lograste en el intento Nro: ",i)
        break
    i = i + 1
else:
    print("Has agotado tus 3 intentos")
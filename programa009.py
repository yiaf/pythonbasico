#https://github.com/yiaf/pythonbasico
#Condicionales elif
print("Menú de Opciones: ")
print("Op 1 = Línea P")
print("Op 2 = Línea 242")
print("Op 3 = Línea AI")
print("Op 4 = Línea AII")
print("Op 5 = Línea B")
tulinea = int(input("Elige tu línea"))
if tulinea == 1:
    print("Viajarás con la Línea P")
elif  tulinea == 2:
    print("Viajarás con la Línea 242")
elif tulinea == 3:
    print("Viajarás con la Línea AI")
elif tulinea == 4:
    print("Viajarás con la Línea AII")
elif tulinea == 5:
    print("Viajarás con la Línea B")
else:
    print("Te irás caminado")

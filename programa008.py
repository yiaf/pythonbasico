#https://github.com/yiaf/pythonbasico
#Condicionales
bn = input("¿Pagaste al BN?")
docs = input("¿Tienes todos tu doctos. en orden?")

if bn == "SI"  and docs == "SI":
    print("Iniciar proceso de Emisión de Constancia")
else:
    print("Falta pagar o docs no están OK")

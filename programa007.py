#https://github.com/yiaf/pythonbasico
#Condicionales
bn  =   input("¿Pagaste al Banco?: ")
docs =   input("¿Tienes todos tu documentos en orden?: ")
if bn == "SI":
    if docs == "SI":
        print("Iniciando proceso de Emitir Constancia de Ingreso")
    else:
        print("Documentos incompletos")
else:
    print("Falta pagar al Banco")


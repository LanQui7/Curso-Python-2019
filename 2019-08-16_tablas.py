valor=int( input("ingresar que tablas quiere imprimir: "))
tvalor = 1
while tvalor < valor:
    for i in range(1,11):
        aux = tvalor*i
        print(tvalor, "x", i, "=", aux)
    print("\n")
    tvalor +=1
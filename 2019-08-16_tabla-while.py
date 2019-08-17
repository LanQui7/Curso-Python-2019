#2019-08-16

valor=int( input("ingresar que tabla quiere imprimir: "))
contador = 1
while contador<11:
    aux = valor*contador
    print(valor, "x", contador, "=", aux )
    contador += 1
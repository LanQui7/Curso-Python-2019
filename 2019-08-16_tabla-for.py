#2019-08-16
valor=int( input("ingresar que tabla quiere imprimir: "))
lista10 = [0,1,2,3,4,5,6,7,8,9,10]
for i in lista10:
    i +=1
    aux = valor*lista10[i]
    print(valor, "x", i, "=", aux )
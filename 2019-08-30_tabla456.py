#2019-08-30 ordenada
print("PROGRAMA PARA IMPRIMIR 3 TABLAS CORRELATIVAS Y ORDENADAS")
valor=int( input("ingresar que tabla correlativa quiere imprimir: "))

for i in range(1,11):
    auxA = valor*i
    auxB = (valor+1)*i
    auxC = (valor+2)*i
    auxD = (valor+3)*i
    print(valor, "x", i, "=", auxA,"\t", valor+1, "x", i, "=", auxB,"\t", valor+2, "x", i, "=", auxC, "\t", valor+3, "x", i, "=", auxD )
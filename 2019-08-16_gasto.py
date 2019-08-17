gasto= int(input("Ingrese cuanto gasto: "))

if gasto <= 100:
    print("pago con efectivo")
elif gasto>100 and gasto<=300:
    print("pago con tarjeta de debito")
elif gasto>300:
    print("pago con tarjeta de credito")
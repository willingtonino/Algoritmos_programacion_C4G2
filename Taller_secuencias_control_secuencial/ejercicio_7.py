"""
Entradas
kilometraje recorrido-->float-->kmr
Salidas
pago-->float-->pago
"""
#Entradas
kmr=float(input("Digita los kilometros recorridos: "))
#Caja negra
if kmr<=300:
    pago=50000#float
elif kmr>300 and kmr<1000:
    pago=70000+(kmr-300)*30000#float
else:
    kmr>1000
    pago=150000+(kmr-1000)*9000#float
    #Salida
print("El dinero a pagar es de:",pago,"COP")
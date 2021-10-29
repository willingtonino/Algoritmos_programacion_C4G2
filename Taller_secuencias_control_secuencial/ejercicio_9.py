"""
Entrada
nombre del comprador-->str-->nombre
monto de la compra-->float-->pago
Salida
nombre del comprador-->str-->nombre
monto de la compra-->float-->pago
monto a pagar-->float-->paga
descuento-->float-->descu
"""
#Entrada
nombre=(input("Ingrese su nombre: "))#str
pago=float(input("Digite el monto de la compra: "))
#Caja negra
if pago<50000:
    paga=pago#float
    descu=0#float
elif pago>=50000 and pago<=100000:
    paga=pago-0.05*pago#float
    descu=5#float
elif pago>100000 and pago<=700000:
    paga=pago-0.11*pago#float
    descu=11#float
elif pago>700000 and pago<=1500000:
    paga=pago-0.18*pago#float
    descu=18#float
else:
    pago>1500000
    paga=pago-0.25*pago#float
    descu=25#float
#Salida
print(nombre,"el monto de la compra es de",pago,"el monto a pagar es de",paga,"el descuento es de",descu,"%")
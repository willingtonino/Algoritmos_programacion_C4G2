"""
Entrada
nombre del comprador-->str-->nombre
monto de la compra-->float-->pago
Salida
monto a pagar-->float-->paga
"""
#Entrada
nombre=(input("Ingrese su nombre: "))#str
pago=float(input("Digite el monto de la compra: "))
#Caja negra
if pago<50000:
    paga=pago
    descu=0
elif pago>=50000 and pago<=100000:
    paga=pago-0.05*pago
    descu=5
elif pago>10000 and pago<=700000:
    paga=pago-0.11*pago
    descu=11
elif pago>700000 and pago<=1500000:
    paga=pago-0.18*pago
    descu=18
else:
    pago>1500000
    paga=pago-0.25*pago
    descu=25
#Salida
print(nombre,"el monto de la compra es de",pago,"el monto a pagar es de",paga,"el descuento es de",descu,"%")
"""
Entradas
Monto de compra-->float-->monto
Salidas
invertir en empresa-->float-->ie
pago a credito-->float-->pc
pagar por interese-->float-->pi
pretamo al banco-->float-->pb
"""
#Entrada
monto=(float(input("Monto a pagar: ")))
if (monto>5000000):
    ie=(monto*0.55)#float
    pb=(monto*0.33)#float
    pc=(monto*0.12)#float
    pi=pc*0.20#float
    print("La cantidad a invertir en los fondos es de:",ie)
    print("la cantidad a pagar de credito es de:",pc)
    print("los interese del credito:",pi)
    print("y el prestamo al banco es de:",pb)
else:
    ie=(monto*0.70)#float
    pc=(monto*0.30)#float
    pi=pc*0.20#float
    #salida
    print("La cantidad a invertir en los fondos es de:",ie)
    print("la cantidad a pagar de credito es de:",pc)
    print("los interese del credito:",pi)
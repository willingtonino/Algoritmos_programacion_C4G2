"""
Entradas
lectura anterios-->int-->lan
lectura actual-->int-->lac
salidas
pago por suscripción-->float-->ps
"""
#Entradas
lan=float(input("Digite la lectura anterior: "))
lac=float(input("Digite la lectura actual: "))
#Caja negra
if ( lan>=0 and lac<=100):
    ps=(lac-lan)*4600#int
elif (lan>=101 and lac<=300):
    ps=(lac-lan)*80000#int
elif (lan>=301 and lac<=500):
    ps=(lac-lan)*100000#int
else: 
    (lan>=501 and lac>501)
    ps=(lac-lan)*120000#int
#Salida
print("El pago total por servicios de luz y aseo es de:",ps)#float
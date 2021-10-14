"""
Entradas
Sueldo base-->float-->Sb
Venta 1-->float-->V1
Venta 2-->float-->V2
Venta 3-->float-->V3
Salidas
comision-->float-->comi
Dinero total-->float-->total
"""
Sb=float(input("Digite sueldo base: "))
V1=float(input("Digite venta 1: "))
V2=float(input("Digite venta 2: "))
V3=float(input("Digite venta 3: "))
#caja negra
comi=(V1+V2+V3)*0.10#float
total=Sb+comi#float
#salidas
print("Por comisión obtendra:",comi, "y el dinero total que recibirá es:",total)
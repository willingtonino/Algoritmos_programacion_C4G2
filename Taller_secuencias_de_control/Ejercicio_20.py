"""
Entradas
Precio decontado-->float-->P
Precio de cuotas-->float-->T
Salidas
Porcentaje de recargo-->float-->porcentaje
"""
#Entradas
P=float(input("Digite el valor del computador por decontado: "))
T=float(input("Digite el valor de cada cuota: "))
#Caja negra
total_cuo=T*12#float
diferencia=total_cuo-P#float
porcentaje=(diferencia*100)/P#float
#Salidas
print("El porcentaje de recargo es de:",porcentaje,"%")
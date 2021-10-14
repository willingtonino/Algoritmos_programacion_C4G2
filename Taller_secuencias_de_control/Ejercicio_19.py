"""
Entradas
lote de naranjas compradas-->int-->X
Precio de naranjas por docena-->float-->Y
Dinero obtenido por la venta de las naranjas-->float-->K
Salidas
Porcentaje de ganancias-->float-->porcentaje
"""
#Entradas
X=int(input("Digite el lote de naranjas compradas: "))
Y=float(input("Digite el precio por docena de las naranjas: "))
K=float(input("Digite el dinero obtenido por la venta de las naranjas: "))
#Caja negra
docenas=X/12
gasto=docenas*Y
ganancias=K-gasto
porcentaje=(ganancias/gasto)*100
#Salidas
print("El porcentaje de ganancias obtenidas es de:",porcentaje,"%")
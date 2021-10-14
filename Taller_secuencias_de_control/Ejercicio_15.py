"""
Entradas
Precio final pagado-->float-->precio_final
Precio de venta al publico-->float-->pvp
Salida
Porcentaje de descuento-->float-->porcentaje
"""
#Entrada
precio_final=float(input("Digite el precio final pagado por el producto: "))
pvp=float(input("Digite el precio de venta al público del producto: "))
#Caja negra
porcentaje=((pvp-precio_final)/pvp)*100#float
#Salida
print("El porcentaje de descuento aplicado es de:",porcentaje,"%")
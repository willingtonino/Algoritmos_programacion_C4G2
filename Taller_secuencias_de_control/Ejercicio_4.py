"""
Entradas
total_pagar-->float-->total_pagar
Salidas
descuento-->float-->descuento
"""
#Entradas
total_pagar=float(input("digite total a pagar: "))
#caja negra
descuento=total_pagar-total_pagar*0.15#float
#salida
print("debe pagar:", descuento)
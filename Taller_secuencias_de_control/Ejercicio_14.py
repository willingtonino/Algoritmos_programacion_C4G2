"""
Entradas
Lectura anterior-->float-->lectura_an
Lectura actual-->float-->lectura_ac
Precio del kilovatio-->float-->costo_k
Salida
Monto a pagar-->float-->monto_actual
"""
#Entradas
lectura_an=float(input("Digite la lectura del mes pasado: "))
lectura_ac=float(input("Digite la lectura actual: "))
costo_k=float(input("Digite el costo del kilovatio: "))
#Caja negra
monto_actual=(lectura_ac-lectura_an)*costo_k#float
#Salida
print("El monto a pagar en el mes es de:",monto_actual)
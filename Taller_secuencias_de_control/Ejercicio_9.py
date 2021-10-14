"""
Entradas
Precio de la hora->float-->precio_h
Horas de trabajo-->float-->horas_t
Salidas
salario neto-->float-->salario_neto
"""
#Entradas
precio_h=float(input("Digite el precio de la hora: "))
horas_t=float(input("Digite las horas trabajadas: "))
#Caja negra
sueldo=precio_h*horas_t#float
salario_neto=sueldo-(sueldo*0.20)#float
#Salidas
print("Su salario neto es de:",salario_neto)
"""
Entradas
Salario bruto-->float-->salario
Salidas
Salario nuevo-->float-->sueldo
"""
#Entrada
salario=float(input("Digite el salario bruto: "))
#Caja negra
sueldo=0
if(salario<900000):
    sueldo=salario*0.15+salario#float
else:
    sueldo=salario*0.12+salario#float
#Salida
print("Su nuevo salario es de:",sueldo)
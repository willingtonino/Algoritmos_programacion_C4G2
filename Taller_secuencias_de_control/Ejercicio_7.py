"""
Entradas
Metros-->float-->metros
Salidas
Pies-->float-->pies
Pulgadas-->float-->pulgadas
"""
#Entradas
metros=float(input("Digite metros: "))
#Caja negra
pies=metros*3.2725#float
pulgadas=metros*39.27#float
#Salidas
print(f"En pies son: {pies}pies y en pulgadas son: {pulgadas}pulgadas")
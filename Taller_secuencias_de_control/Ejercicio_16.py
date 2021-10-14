"""
Entradas
Galones-->float-->galones
Salidas
Precio-->float-->precio
"""
#Entradas
galones=float(input("Digite número de galones: "))
#Caja negra
precio=galones*3.785*50000#float
#Salida
print("El cliente debe pagar:",precio,"COP")
"""
Entrada
Valores (p,q)-->int-->valores
Salidas
resultado-->int-->resultado
"""
#Entradas
valores=(input("Ingresa los valores de P y Q: "))
(p,q)=valores.split(" ")
p=int(p)
q=int(q)
#Caja negra
resultado=(p**3)+(q**4)-2*p**2#int
if resultado>680:
    #salida
    print(p,"y",q,"satisfacen la expresión")
else:
    #salida
    print(p,"y",q,"no satisfacen la expresión")
"""
Entradas
A-->float-->A
B-->float-->B
C-->float-->C
Salidas
X1-->float-->X1
X2-->float-->x2
"""
#Entrada
Datos=input("Digite los tres valores: ")
(A,B,C)=Datos.split(" ")
A=float(A)
B=float(B)
C=float(C)

#Caja negra
D=(B**2)-4*A*C
if D==0:
    X1 = X2 =-B/(2*A)#float
elif D>0:
    X1 = (-B+(B**2-4*A*C)**(0.5))/(2*A)#Float
    X2 = (-B-(B**2-4*A*C)**(0.5))/(2*A)#Float
else:
    D<0
    X1 = X2 ="No tiene solución en los reales"
#Salida
print("El valor de X1 es:",X1,"y el valor de X2 es:",X2)
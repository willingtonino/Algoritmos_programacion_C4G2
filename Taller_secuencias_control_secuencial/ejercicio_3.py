"""
Entradas
datos(a,b,c)--->int--->x
Salida
resultado-->int-->resul
"""
#Entrada
x=(input("ingrese los datos: "))
(a,b,c,d)=x.split(" ")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
#Caja negra
if (d==0):
    resul=(a-b)**2#int
    #salida
    print("El resultado es:",resul)
elif (d>0):
    resul=((a-b)**3)/d#float
    #salida
    print("El resultado es:",resul)
else:
    #salida
    print("No se encontro operación")
"""
Salidas
Valores de k antes de que la sumatoria de los más cercano a 1000
"""
k=1
e=0
a=0
#Caja negra
print()
while(e<=1000):
    e=((k**2)+1)/k
    k=k+1
    a=a+1
    if e>=1000:
        e=((k**2)+1)/k
        k=k+1
        a=a-1
        break
    #salida
    print (a)

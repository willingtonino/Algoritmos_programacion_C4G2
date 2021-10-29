"""
Salidas
Valores de k antes de que la sumatoria de los más cercano a 1000
"""
k=1
e=0
h=0
a=0
#Caja negra
print()
while(h<=1000):
    e=((k**2)+1)/k
    k=k+1
    a=a+1
    if h<=1000:
        h=h+e
    if h>=1000:
        e=((k**2)+1)/k
        k=k+1
        a=a-1
        h=h-e  
        break
    #salida
    print (a, end=", ")
print("\n") 

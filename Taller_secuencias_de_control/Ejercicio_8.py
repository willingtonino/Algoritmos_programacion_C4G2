"""
Entradas
Lado 1-->float-->lado1
Lado 2-->float-->lado2
Lado 3-->float-->lado3
Salidas
Area del triangulo-->float-->area
"""
#Entradas
lado1=float(input("Digite lado 1: "))
lado2=float(input("Digite lado 2: "))
lado3=float(input("Digite lado 3: "))
#Caja negra
s=(lado1+lado2+lado3)/2#float
area=(s*(s-lado1)*(s-lado2)*(s-lado3))**(1/2)#float
#Salida
print("El areá del triangulo es de:",area)
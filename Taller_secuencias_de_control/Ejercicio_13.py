"""
Entradas
Billetes de cincuenta mil-->int-->N1
Billetes de veinte mil-->int-->N2
Billetes de diez mil-->int-->N3
Billetes de cinco mil-->int-->N4
Billetes de dos mil-->int-->N5
Billetes de mil-->int-->N6
Billetes de quinientos-->int-->N7
Billetes de cien-->int-->N8
Salidas
Cantidad de dinero-->float-->total
"""
#Entradas
N1=int(input("Digite número de los billetes de 50000: "))
N2=int(input("Digite número de los billetes de 20000: "))
N3=int(input("Digite número de los billetes de 10000: "))
N4=int(input("Digite número de los billetes de 5000: "))
N5=int(input("Digite número de los billetes de 2000: "))
N6=int(input("Digite número de los billetes de 1000: "))
N7=int(input("Digite número de los billetes de 500: "))
N8=int(input("Digite número de los billetes de 100: "))
#Caja negra
total=(N1*50000+N2*20000+N3*10000+N4*5000+N5*2000+N6*1000+N7*500+N8*100)#float
#Salidas
print("El dinero total que hay en el banco es de:",total)
"""
Entradas
edad 1-->int-->edad_uno
edad 2-->int-->edad_dos
edad 3-->int-->edad_tres
Salida
Promedio de las tres edades-->float-->prome
"""
edad_uno=int(input("digite edad 1: "))
edad_dos=int(input("digite edad 2: "))
edad_tres=int(input("digite edad 3: "))
#caja negra
prome=(edad_uno+edad_dos+edad_tres)/3#float
#salida
print("El promedio de las tres edades es:",prome)
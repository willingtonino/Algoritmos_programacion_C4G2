Alcool=0
Gasolina=0
Diesel=0
while True:
    combus=int(input())
    if combus==1:
        Alcool=Alcool+1
    elif combus==2:
        Gasolina=Gasolina+1
    elif combus==3:
        Diesel=Diesel+1
    elif combus==4:
        break
    else:
        combus==combus
print("MUITO OBRIGADO")
print(Alcool)
print(Gasolina)
print(Diesel)





















"""
Entradas: Valores enteros correspondientes al tipo de gas
Tipo de gas --> int --> A
Salidas: 4 valores str con las respectiva cantidades de cada gas
MUITO OBRIGADO --> str --> B
Alcool --> str --> Alcool
Gasolina --> str --> Gasolina
Diesel --> str --> Diesel

# Caja negra
Alcool = 0 
Gasolina = 0 
Diesel = 0
while True:
    A = int(input()) # Entradas
    if A == 1: 
        Alcool += 1
    elif A == 2: 
        Gasolina += 1
    elif A == 3:
        Diesel += 1
    elif A == 4:
        break
    else: 
        A = A

# Salidas
print("MUITO OBRIGADO")
print("Alcool:",Alcool)
print("Gasolina:",Gasolina)
print("Diesel:",Diesel)
"""
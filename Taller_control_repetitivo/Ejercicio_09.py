"""
Entrada
combustible-->int-->combus
salidas
muchas gracias-->str-->MUITO OBRIGADO
alcohol-->int-->Alcool
gasolina-->int-->Gasolina
diesel-->int-->Diesel
"""
Alcool=0
Gasolina=0
Diesel=0
#Caja negra
while True:
    #Entrada
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
#Salidas        
print("MUITO OBRIGADO")
print("Alcool:",Alcool)
print("Gasolina:",Gasolina)
print("Diesel:",Diesel)
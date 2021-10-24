"""
Entrada
temperatura-->float-->temp
Salidas
Deporte-->str-->deporte
"""
#Entrada
temp=str(input("Ingrese la temperatura"))
#Caja negra
deporte=""
if(temp>85):#float
    deporte="Natación"
elif(temp>70 and temp<=85):#float
    deporte="Tenis"
elif(temp>32 and temp<=70):#float
    deporte="Golf"
elif(temp>10 and temp<=32):#float
    deporte="Esquí"
elif(temp<=10):#float
    deporte="Marcha"
else:
    deporte="No se encuentra deporte con esta temperatura"
#Salida
print(deporte)
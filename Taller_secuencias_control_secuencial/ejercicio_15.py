"""
Entradas
Edad-->int-->edad
nivel de hemoglobina-->float-->nh
sexo-->int-->sexo
Salida
resultado de anemia-->str-->resultado
"""
#Entrada
edad=int(input("Ingrese su edad en meses: "))
nh=float(input("Digite su nivel de hemogoblina en g%: "))
if edad>180:
    sexo=input("¿Su sexo es masculino o femenino?:\n1 para masculino\n2 para femenino\n")
else:
    sexo=0
sexo=int(sexo)
#Caja negra
if edad>=0 and edad<=1:
    if nh>=13 and nh<=26:
        resultado="negativo"
    elif nh<13:
        resultado="Positivo"
    else:
        nh>26
        resultado="Error"
elif edad>1 and edad<=6:
    if nh>=10 and nh<=18:
        resultado="Negativo"
    elif nh<10:
        resultado="Positivo"
    else:
        nh>18
        resultado="Error"
elif edad>6 and edad<=12:
    if nh>=11 and nh<=15:
        resultado="Negativo"
    elif nh<11:
        resultado="Positivo"
    else:
        nh>15
        resultado="Error"
elif edad>12 and edad<=60:
    if nh>=11.5 and nh<=15:
        resultado="Negativo"
    elif nh<11.5:
        resultado="Positivo"
    else:
        nh>15
        resultado="Error"
elif edad>60 and edad<=120:
    if nh>=12.6 and nh<=15.5:
        resultado="Negativo"
    elif nh<12.6:
        resultado="positivo"
    else:
        nh>15.5
        resultado="Error"
elif edad>120 and edad<=180:
    if nh>=13 and nh<=15.5:
        resultado="Negativo"
    elif nh<13:
        resultado="Positivo"
    else:
        nh>15.5
        resultado="Error"
elif edad>180 and sexo==2:
        if nh>=12 and nh<=16:
            resultado="Negativo"
        elif nh<12:
            resultado="Positivo"
        else:
            nh>16
            resultado="Error"
elif edad>180 and sexo==1:
        if nh>=14 and nh<=18:
            resultado="Negativo"
        elif nh<14:
            resultado="Positivo"
        else:
            nh>18
            resultado="Error"
#Salida
print("Su estado en anemia es:",resultado)
"""
Entradas
Fecha de nacimiento-->int-->fecha
Salidas
Edad-->int-->edad
Signo zodiacal-->str-->signo
"""
from datetime import date
#Entrada
fecha=input("Digite su fecha de nacimiento en el formato dia/mes/año ")
(dia,mes,año)=fecha.split(" ")
dia=int(dia)
mes=int(mes)
año=int(año)

año_ac=date.today().year
mes_ac=date.today().month
dia_ac=date.today().day
#Caja negra
edad=año_ac-año
if mes<=mes_ac and dia<=dia_ac:
        edad=edad
elif mes<mes_ac:
    edad=edad
else:
    edad=edad-1


if dia>=22 and mes==11 or dia<=21 and mes==12:
    signo="sagitario"
elif dia>=22 and mes==12 or dia<=20 and mes==1:
    signo="capricornio"
elif dia>=21 and mes==1 or dia<=19 and mes==2:
    signo="acuario"
elif dia>=20 and mes==2 or dia<=19 and mes==3:
    signo="piscis"
elif dia>=21 and mes==3 or dia<=20 and mes==4:
    signo="aries"
elif dia>=21 and mes==4 or dia<=21 and mes==5:
    signo="tauro"
elif dia>=22 and mes==5 or dia<=21 and mes==6:
    signo="Géminis"
elif dia>=22 and mes==6 or dia<=22 and mes==7:
    signo="cáncer"
elif dia>=23 and mes==7 or dia<=23 and mes==8:
    signo="leo"
elif dia>=24 and mes==8 or dia<=22 and mes==9:
    signo="virgo"
elif dia>=23 and mes==9 or dia<=22 and mes==10:
    signo="libra"
else:
    dia>=23 and mes==10 or dia<=22 and mes==11
    signo="escorpión"
#Salida
print("Su edad es",edad,"y su signo zodiacal es",signo)
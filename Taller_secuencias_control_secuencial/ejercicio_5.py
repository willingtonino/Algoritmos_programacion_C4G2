"""
Entradas
Departamentos(D1, D2, D3)-->float-->D
sueldo-->float-->Suel
Salida
Sueldo_departamento_1-->float-->SD1
Sueldo_departamento_2-->float-->SD2
Sueldo_departamento_3-->float-->SD3
"""
#Entrada
Suel=float(input("Digite sueldo: "))
D=(input("Digite los ingresos de los tres departamentos: "))
(D1,D2,D3)=D.split(" ")
D1=int(D1)
D2=int(D2)
D3=int(D3)
#Caja negra
Sd=float(D1+D2+D3)
P=float(Sd*0.33)
if D1>P and D2>P and D3>P:
    SD1=float((Suel*0.20)+Suel)
    SD2=float((Suel*0.20)+Suel)
    SD3=float((Suel*0.20)+Suel)
elif D1>P and D2>P:
    SD1=float((Suel*0.20)+Suel)
    SD2=float((Suel*0.20)+Suel)
    SD3=Suel
elif D1>P and D3>P:
    SD1=float((Suel*0.20)+Suel)
    SD3=float((Suel*0.20)+Suel)
    SD2=Suel
elif D2>P and D3>P:    
    SD1=Suel
    SD2=float((Suel*0.20)+Suel)
    SD3=float((Suel*0.20)+Suel)
elif D1>P:
    SD1=float((Suel*0.2)+Suel)
    SD2=Suel
    SD3=Suel
elif D2>P:
    SD2=float((Suel*0.2)+Suel)
    SD1=Suel
    SD3=Suel
else:
    D3>P
    SD3=float((Suel*0.2)+Suel)
    SD1=Suel
    SD2=Suel
print("Los del depatamento 1 ganaron:",SD1)
print("Los del depatamento 2 ganaron:",SD2)
print("Los del depatamento 3 ganaron:",SD3)
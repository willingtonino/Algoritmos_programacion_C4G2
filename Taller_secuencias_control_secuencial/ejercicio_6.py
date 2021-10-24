"""
Entradas
numero(A,B,C,D)-->int-->entero
Salida
numero A-->int-->entea
numero B-->int-->enteb
numero C-->int-->entec
numero D-->int-->ented
"""
#Entrada
entero=input("Digite los cuatro números: ")
(A,B,C,D)=entero.split(" ")
A=int(A)
B=int(B)
C=int(C)
D=int(D)
#Caja negra
if A==A and B==0 and C==0 and D==0:
    entea=A#int
    enteb=B#int
    entec=C#int
    ented=D#int
elif A>=1 and B>=5 and C>=0 and D>=0:
    entea=A+1#int
    enteb=B*0#int
    entec=C*0#int
    ented=D*0#int
elif A>=1 and B<5 and C>=0 and D>=0:
    entea=A-1#int
    enteb=B*0#int
    entec=C*0#int
    ented=D*0#int
elif A==0 and B>=5 and C>=0 and D>=0:
    entea=A+1#int
    enteb=B*0#int
    entec=C*0#int
    ented=D*0#int
else:
    A==0 and B<5 and C>=0 and D>=0
    entea=A#int
    enteb=B*0#int
    entec=C*0#int
    ented=D*0#int
#Salida
print("El número entero es:",entea,enteb,entec,ented)
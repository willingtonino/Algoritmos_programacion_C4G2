"""
Entradas
cantidad de dinero-->float-->cd
Salidas
Billetes de 100000-->int-->db
Billetes de 50000-->int-->c1
Billetes de 20000-->int-->c2
Billetes de 10000-->int-->c3
Billetes de 5000-->int-->c4
Billetes de 2000-->int-->c5
Billetes de 1000-->int-->c6
Monedas de 500-->int-->c7
Monedas de 200-->int-->c8
Monedas de 100-->int-->c9
Monedas de 50-->int-->c10
"""
#Entradas
cd=float(input("Digite la cantidad de dinero: "))
#Caja negra

db=(cd-cd%100000)/100000#float
cd=cd%100000#float

c1=(cd-cd%50000)/50000#float
cd=cd%50000#float

c2=(cd-cd%20000)/20000#float
cd=cd%20000#float

c3=(cd-cd%10000)/10000#float
cd=cd%10000#float
                
c4=(cd-cd%5000)/5000#float
cd=cd%5000#float
                    
c5=(cd-cd%2000)/2000#float
cd=cd%2000#float
                        
c6=(cd-cd%1000)/1000#float
cd=cd%1000#float
                            
c7=(cd-cd%500)/500#float
cd=cd%500#float
                                
c8=(cd-cd%200)/200#float
cd=cd%200#float
                                    
c9=(cd-cd%100)/100#float
cd=cd%100#float
                                        
c10=(cd-cd%50)/50#float

if cd>0:
    #salida
    print("Los billetes de 100000 son:",db)
if c1>0:
    #salida
    print("Los billetes de 50000 son:",c1)
if c2>0:
    #salida
    print("Los billetes de 20000 son:",c2)
if c3>0:
    #salida
    print("Los billetes de 10000 son:",c3)
if c4>0:
    #salida
    print("Los billetes de 5000 son:",c4)
if c5>0:
    #salida
    print("Los billetes de 2000 son:",c5)
if c6>0:
    #salida
    print("Los billetes de 1000 son:",c6)
if c7>0:
    #salida
    print("Los billetes de 500 son:",c7)
if c8>0:
    #salida
    print("Los billetes de 200 son:",c8)
if c9>0:
    #salida
    print("Los billetes de 100 son:",c9)
if c10>0:
    #salida
    print("Los billetes de 50 son:",c10)
else:
    #salida
    print("Esta cantidad de dinero no tiene billete")
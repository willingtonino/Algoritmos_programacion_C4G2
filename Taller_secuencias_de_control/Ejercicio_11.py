"""
Entradas
Nombre-->str-->nombre
Número de hijos-->int-->hijos
Horas normales trabajadas-->float-->horas_n
Valor de la hora-->float-->valor_h
Horas extra trabajadas-->float-->horas_extra
Salidas
Asignaciones-->float-->asig
Deducciones-->float-->dedu
Sueldo neto-->float-->sueldo_neto
"""
#Entradas
nombre=str(input("Ingrese su nombre: "))
hijos=int(input("Digite su numero de hijos: "))
horas_n=float(input("Digite las horas normales trabajadas: "))
valor_h=float(input("Digite el valor de la hora normal de trabajo: "))
horas_extra=float(input("Digite las horas extra trabajadas: "))
#Caja negra
sueldo_n=valor_h*horas_n#float
valor_hx=valor_h+(valor_h*0.25)#float
sueldo_hx=horas_extra*valor_hx#float
sueldo_b=sueldo_n+sueldo_hx#float
dedu=sueldo_b*0.05+sueldo_b*0.02+sueldo_b*0.07#float
asig=250000+173000*hijos+180000#float
sueldo_neto=sueldo_b-dedu+asig#float
#Salidas
print(nombre,"sus asignaciones son de:",asig,"COP. Sus deducciones son de:",dedu,"COP. Su salario neto es de:",sueldo_neto,"COP")
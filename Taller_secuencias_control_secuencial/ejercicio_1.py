"""
Entradas
capital a invertir-->float-->capital
tasa de interes-->float-->tinteres
Salida
dinero total-->float-->saldo
"""
#Entrada
capital=(float(input("Digite el dinero invertido en el banco: ")))
tinteres=(float(input("Digite la tasa de interes en porcentaje: ")))
#Caja negra
interes=capital*(tinteres/100)#float
saldo=capital+interes#float
if(interes>100000):
    #Salida
    print("Puede reinvertir sus intereses que son de: ",interes,"COP")
else:
    #Salida
    print("No reinvierta sus intereses que son de: ",interes,"COP")
#Salida
print("Su saldo total es de: ",saldo,"COP")
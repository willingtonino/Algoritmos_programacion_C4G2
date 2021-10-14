"""
Entradas
Prestamo de Bolívares-->float-->Bolivares_X
Intereses pagadas en cuatro años-->float-->Bolivares_Y
Salidas
Porcentaje anual que se cobro-->float-->tasa_interes
"""
#Entradas
Bolivares_X=float(input("Digite valor del prestamo: "))
Bolivares_Y=float(input("Digite valor de los intereses pagados: "))
#Caja negra
tasa_interes=(Bolivares_Y*100)/(Bolivares_X*4)#float
#Salida
print("El porcentaje cobrado anualmente:",tasa_interes)
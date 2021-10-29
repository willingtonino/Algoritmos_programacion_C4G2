"""
Escriba un programa que imprima todos los enteros positivos 
impares menores que 100 omitiéndose aquellos que sean 
divisibles por 7
Salida
Contador-->int-->contador
"""
contador=0
#Caja negra
while(contador<100):
    if(contador%3==0) and (contador%7!=0):
        #Salida
        print(contador)
    contador=contador+1 

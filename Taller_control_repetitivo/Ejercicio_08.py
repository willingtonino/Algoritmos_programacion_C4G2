"""
Entradas
contraseña-->int-->contraseña
Salidas
correcto-->str-->Acesso Permitido
incorrecto-->str-->Senha Invalida
"""
#Caja negra
while True:
    #Entrada
    contraseña=int(input())
    #Caja negra
    if(contraseña==2002):
        #Salida
        print("Acesso Permitido")
        break
    else:
        #Salida
        print("Senha Invalida")
"""
Entradas
Chelines austríacos-->float-->Ca
Dracmas griegos-->float-->Dg
Pesetas-->float-->Pe
Salidas
Pesetas Convertidas-->float-->Pse
Francos franceses-->float-->ff
Dólares-->float-->dl
Liras italianas-->float-->li
"""
#Entradas
Ca=float(input("Digite la cantidad de Chelines austríacos: "))
Dg=float(input("Digite la cantidad de Dracmas griegos: "))
Pe=float(input("Digite la cantidad de Pesetas: "))
#Caja negra
Pse=(956.871/100)*Ca#Float
ff=Dg*(88.607/100)/20.110#Float
dl=Pe/122.499#Float
li=(100/9.289)*Pe#Float
#Salidas
print(Ca,"chelines austriacos son",Pse,"pesetas")
print(Dg,"dracmas griegos son",ff,"francos franceses")
print(Pe,"pesetas son",dl,"dólares y en liras italianas son",li,"liras italianas")
"""
Entradas
Divisor-->int-->Divi
Dividendo-->int--divide
Salida
Restas efectuadas
cociente-->float-->coci
resto-->int-->res
"""
#Entrada
Divi=int(input("Digite el divisor: "))
divide=int(input("Digite el dividendo: "))

A=int(Divi/divide)
C=0
for i in range(A):
    print(Divi,"-",divide,"=",Divi-divide)
    Divi=int(Divi-divide)
    C=C+1
#Salida
print("El cociente es",C,"y el resto es",Divi)

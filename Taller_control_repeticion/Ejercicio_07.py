"""
Entradas
(X,M)-->int-->valores
Salida
Nueva experiencia Monster-->int-->E
"""
#Caja negra
while True:
    #Entrada
    valores=input("")
    (X,M)=valores.split(" ")
    X=int(X)
    M=int(M)
    #Caja negra
    if (X==0) and M==0:
        break
    else:
        E=X*M
    #Salida
    print(E)
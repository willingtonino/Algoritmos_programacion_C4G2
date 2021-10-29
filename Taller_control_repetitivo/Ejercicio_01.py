"""
Entradas
(N,K)-->int-->numero
Salidas
N-->int-->N con el mismo valor de K
"""
#Entrada
numero=input("Digite dos numeros enteros positivos: ")
(N,K)=numero.split(" ")
N=int(N)
K=int(K)
#Caja negra
if K<N:
    while K<=N:
        #Salida
        print(N)
        N=N-1
else:
    #Salida
    print("Intenta que el primero sea mayor que el segundo ")
frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')

lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
for i in frutas:
  lista_frutas.append(i)

lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in numeros:
  lista_numeros.append(i)

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista(str)-->list-->lista
elemento-->str-->elem
Salidas:
lista(str)-->list-->a,b
"""
def eliminar_un_caracter_de_toda_la_lista(lista:list,elem:str)->list:
  aux=[]
  for i in lista:
    a=i.replace(elem,"")
    aux.append(a)
  return aux



#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
lista(str)-->list-->lista
Salidas:
lista(str)-->list-->lista_frutas
lista(str)-->list-->lista_numeros
"""
def copia_lista(lista:list)->list:
  return lista.copy() 



#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista(str)-->list-->lista
Salidas:
lista(int)-->list-->pares
"""  
def numeros_pares(lista:list)->list:
  aux=[]
  for i in lista:
    if(int(float(i)%2==0)):
      aux.append(i) 
  return aux



#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista(str)-->list-->lista
elemento-->str-->elem
Salidas:
lista(str)-->list-->lista elemento
"""  
def elimina_elemento_lista(lista:list,elem:str)->list:
  lista.remove(elem)
  return lista



#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista(str)-->list-->lista
elem-->str-->elem
Salidas:
lista letra-->list-->lista(str)
"""  
def letra(lista:list,elem:str)->list:
  aux=[]
  for i in lista:
    if(i[0]==elem):
      aux.append(i)
  return aux



#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista(str)-->list-->lista
Salidas:
lista(str)-->list-->lista
"""   
def tamano_lista(lista:list)->list:
  aux=[]
  a=len(lista)
  aux.append(a)
  return aux



#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista(str)-->list-->lista
Salidas:
a-->int-->tamaño
b-->str-->tipo
"""  
def informacion_lista(lista:list)->list:
  aux=[]
  a=len(lista)
  b=type(lista[0])
  aux.append(a)
  aux.append(b)
  return aux
#Retornar una lista con los numero negativos  
"""
Entradas:
lista(str)-->list-->lista
Salidas:
lista(str)-->list-->lista negativos
"""  
def numeros_negativos(lista:list)->list:
  aux=[]
  for i in lista:
    if(i[0]=="-"):
      aux.append(i)
  return aux



#realizar una funcion que retorne la posicion de un elemento que pasa por parametro

"""
Entradas:
lista(str)-->list-->lista
elemento-->str-->elem
Salidas:
lista(str)-->list-->lista
"""  
def posicion_elemento(lista:list,elem:str)->list:
  aux=[]
  conta=0
  for i in lista:
    if elem==i:
      conta=conta+1
      break
    else:
      conta=conta+1
  aux.append(conta)
  return aux



#realizar una funcion que agregue al final de archivo frutas una fruta
"""
Entradas:
lista(str)-->list-->frutas
elemento-->str-->elem
Salidas:
lista(str)-->list-->frutas
"""
def frutas(elem:str)->list:
  aux=open("frutas.txt","a")
  aux.write(elem)
  aux.close()



#Realizar una funcion que cuente el numero de veces que se repite un elemento  
"""
Entradas:
lista(str)-->list-->lista
Salidas:
lista(str)-->list-->lista
"""
def repetir(lista:list,elem:str):
  aux=[]
  conta=0
  for i in lista:
    e=i.replace("\n","")
    if e==elem:
      conta=conta+1
  aux.append(conta)
  return aux



""" 
if __name__ == "__main__":
  lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy)
"""

#Solucion

"""

if __name__ == "__main__":
  a=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  b=eliminar_un_caracter_de_toda_la_lista(lista_numeros,"\n")
  print(a)
  print(b)
"""

"""
if __name__ == "__main__":
  print(copia_lista(lista_frutas))
  print("\n")
  print(copia_lista(lista_numeros))
"""

"""
if __name__ == "__main__":
  pares=numeros_pares(lista_numeros)
  print(pares)
"""

"""
if __name__ == "__main__":
  print(elimina_elemento_lista(lista_frutas,"Fresa\n"))
  print(elimina_elemento_lista(lista_numeros,"123\n"))
"""

"""
if __name__ == "__main__":
  print(letra(lista_frutas,"A"))
"""

"""
if __name__ == "__main__":
  print(tamano_lista(lista_frutas))
  print(tamano_lista(lista_numeros))
"""

"""
if __name__ == "__main__":
  print(informacion_lista(lista_frutas))
"""

"""
if __name__ == "__main__":
  print(numeros_negativos(lista_numeros))
"""

"""
if __name__ == "__main__":
  print(posicion_elemento(lista_frutas,"Fresa\n"))
  print(posicion_elemento(lista_numeros,"32\n"))
"""

"""
if __name__ == "__main__":
  frutas("\nLulo")
"""

"""
if __name__ == "__main__":
  print(repetir(lista_numeros,"32"))
"""

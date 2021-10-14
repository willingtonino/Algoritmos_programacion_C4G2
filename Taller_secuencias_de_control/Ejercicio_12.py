"""
Entradas
Examen de matemáticas-->float-->mat_exa
tarea de matemáticas 1-->float-->mat1
tarea de matemáticas 2-->float-->mat2
tarea de matemáticas 3-->float-->mat3
Examen de física-->float-->fis_exa
tarea de física 1-->float-->fis1
tarea de física 2-->float-->fis2
Examen de química-->float-->qui_exa
tarea de química 1-->float-->qui1
tarea de química 2-->float-->qui2
tarea de química 3-->float-->qui3
Salidas
promedio de matemáticas-->float-->promedio_mat
promedio de física-->float-->promedio_fis
promedio de química-->float-->promedio_qui
promedio de general-->float-->promedio_gen
"""
#Salida
mat_exa=float(input("Digite nota del examen de matemáticas: "))
mat1=float(input("Digite nota 1 tarea de matemáticas: "))
mat2=float(input("Digite nota 2 tarea de matemáticas: "))
mat3=float(input("Digite nota 3 tarea de matemáticas: "))
fis_exa=float(input("Digite nota del examen de física: "))
fis1=float(input("Digite nota 1 tarea de física: "))
fis2=float(input("Digite nota 2 tarea de física: "))
qui_exa=float(input("Digite nota del examen de química: "))
qui1=float(input("Digite nota 1 tarea de química: "))
qui2=float(input("Digite nota 2 tarea de química: "))
qui3=float(input("Digite nota 3 tarea de química: "))
#Caja negra
promedio_mat=(((mat1+mat2+mat3)/3)*0.10)+(mat_exa*0.90)
promedio_fis=fis_exa*0.80+((fis1+fis2)/2)*0.20
promedio_qui=qui_exa*0.85+((qui1+qui2+qui3)/3)*0.15
promedio_gen=(promedio_mat+promedio_fis+promedio_qui)/3
#Salida
print("Su promedio en matemáticas es de:",promedio_mat)
print("Su promedio en física es de:",promedio_fis)
print("Su promedio en química es de:",promedio_qui)
print("Su promedio general es de:",promedio_gen)

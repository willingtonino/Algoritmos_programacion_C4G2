"""
Entradas
calificacion parcial 1-->float-->calificacion_parcial1
calificacion parcial 2-->float-->calificacion_parcial2
calificacion parcial 3-->float-->calificacion_parcial3
ccalificación del examen final-->float-->calificacion_examen
calificación del trabajo final-->float-->calificacion_trabajo
salidas
calificación final-->float-->total_porcentajes
"""
#Entradas
calificacion_parcial1=float(input("Digite calificación parcial 1: "))
calificacion_parcial2=float(input("Digite calificación parcial 2: "))
calificacion_parcial3=float(input("Digite calificación parcial 3: "))
calificacion_examen=float(input("Digite calificación del examen final: "))
calificacion_trabajo=float(input("Digite calificación del trabajo final: "))
#Caja negra
porcentaje_parciales=((calificacion_parcial1+calificacion_parcial2+calificacion_parcial3)/3)*0.55
porcentaje_examen_final=calificacion_examen*0.30
porcentaje_trabajo_final=calificacion_trabajo*0.15
total_porcentajes=porcentaje_parciales+porcentaje_examen_final+porcentaje_trabajo_final
#Salidas
print("Su calificación final de la materia de computacion es :", total_porcentajes)
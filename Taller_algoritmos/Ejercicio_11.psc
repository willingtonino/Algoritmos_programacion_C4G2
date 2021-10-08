Algoritmo Inicio_calificacion_final
	Escribir "Digite calificación del parcial 1"
	Leer calificacion_parcial1
	Escribir "Digite calificación del parcial 2"
	Leer calificacion_parcial2
	Escribir "Digite calificación del parcial 3"
	Leer calificacion_parcial3
	promedio_parciales<-(calificacion_parcial1+calificacion_parcial2+calificacion_parcial3)/3
	porcentaje_parciales<-promedio_parciales*0.55
	Escribir "Digite calificación del examen final"
	Leer calificacion_examen
	porcentaje_examen_final<-calificacion_examen*0.30
	Escribir "Digite calificación del trabajo final"
	Leer calificacion_trabajo
	porcentaje_trabajo_final<-calificacion_trabajo*0.15
	total_porcentajes<-porcentaje_parciales+porcentaje_examen_final+porcentaje_trabajo_final
	Escribir "Su calificación final de la materia de Algoritmos es:" total_porcentajes
FinAlgoritmo
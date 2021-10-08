Algoritmo Inicio_sueldo_comision
	Escribir "Digite la venta 1"
	Leer venta_1
	Escribir "Digite la venta 2"
	Leer venta_2
	Escribir "Digite la venta 3"
	Leer venta_3
	Escribir "Digite su sueldo base"
	Leer sueldo
	comision<-(venta_1+venta_2+venta_3)*0.10
	total_ganado<-comision+sueldo
	Escribir "Dinero obtenido por comisiones :" comision
	Escribir "El total que recibirá en el mes: " total_ganado
FinAlgoritmo

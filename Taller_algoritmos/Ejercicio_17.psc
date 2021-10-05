Algoritmo Inicio_vehiculo
	Escribir "Nota: 1. la velocidad debe ser en kilometros por hora y la distancia en kilometros;"
	Escribir " 2. la velocidad del vehiculo que va atras debe ser mayor a la del vehiculo 1"
	Escribir " Digite la distancia entre los dos autos"
	Leer distacia
	Escribir "Velocidad del vehiculo delantero"
	Leer vehiculo_1
	Escribir "Velocidad del vehiculo de atras"
	Leer vehiculo_2
	Si vehiculo_2 > vehiculo_1 Entonces
		tiempo<-distacia/(vehiculo_2-vehiculo_1)
		minutos<-60*tiempo
		Escribir "El tiempo que tardara el vehiculo de atras en alcanzar al de adelante es:" minutos " minutos"
	SiNo
		Escribir "Error: dato no valido"
	Fin Si
	
	
FinAlgoritmo

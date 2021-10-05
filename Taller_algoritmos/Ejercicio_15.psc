Algoritmo Inicio_invertir
	Escribir "Digite número de dos cifras"
	Leer numero_in
	Si numero_in >= 10 y numero_in <= 99 Entonces
		numero_1 = trunc(numero_in/10)
		numero_2 = numero_in mod 10
		Escribir "El número invertido es:" numero_2 numero_1
	SiNo
		Escribir "Número no valido"
	Fin Si
FinAlgoritmo

Algoritmo Inicio_invertir
	Escribir "Digite n�mero de dos cifras"
	Leer numero_in
	Si numero_in >= 10 y numero_in <= 99 Entonces
		numero_1 = trunc(numero_in/10)
		numero_2 = numero_in mod 10
		Escribir "El n�mero invertido es:" numero_2 numero_1
	SiNo
		Escribir "N�mero no valido"
	Fin Si
FinAlgoritmo

import time                     # Importa la librería para manejar tiempos y pausas

cadena = 'Python'               # Define la cadena de texto a recorrer

for letra in cadena:            # Itera letra por letra en la palabra
	if letra == 't':            # Si la letra actual es 't'...
		continue                # Omite esta iteración y pasa a la siguiente letra
	print(letra)                # Imprime la letra actual
	time.sleep(1)               # Detiene la ejecución del programa durante 1 segundo

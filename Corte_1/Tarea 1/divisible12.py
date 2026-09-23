for i in range(100, 301):       # Itera desde el número 100 hasta el 300
	if (i % 12) != 0:           # Si el residuo de dividir entre 12 es diferente de 0...
		continue                # Salta a la siguiente iteración, ignorando el resto del bucle
	print(i)                    # Imprime el número solo si es múltiplo de 12

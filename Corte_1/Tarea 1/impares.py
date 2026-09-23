for i in range(1, 21):          # Recorre los números del 1 al 20
	residual = i % 2            # Saca el residuo de dividir entre 2
	if residual == 0:           # Si el residuo es 0, el número es par
		print(f'{i} is even')
	else:
		print(str(i) + ' is odd')  # Si no, el número es impar

for i in range(0, 6):           # Recorre del 0 al 5
	result = i ** 3             # Eleva el número al cubo
	print(result)               # Muestra el resultado de la potencia

times = input("Enter a number of times: ")  # Pide un número límite de repeticiones
times = float(times)            # Lo convierte temporalmente a float por seguridad
times = int(times)              # Lo convierte a entero final
print(type(times))              # Muestra el tipo de dato
print(times)                    # Imprime el valor de 'times'

if times == 0:                  # Si el número ingresado es 0
	print("Don't do anything")
else:                           # Si es mayor a 0, ejecuta un bucle de tamaño 'times'
	for i in range(1, times + 1):
		print("i = ", i)

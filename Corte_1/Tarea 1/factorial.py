while True:                     # Bucle infinito hasta que se interrumpa manualmente

    value = int(input("Enter a positive integer value: "))  # Pide un valor y lo convierte a entero
    print("Value: ", value)     # Muestra el valor ingresado
    a = isinstance(value, int)  # Verifica si 'value' es de tipo entero (devuelve True)
    if a == True and value > 0: # Comprueba si es entero y además mayor a cero
        fact = 1                # Inicializa la variable acumuladora para el factorial
        for i in range (1, value + 1):  # Itera desde 1 hasta el número ingresado
            fact = fact*i       # Multiplica acumulativamente para hallar el factorial
        print(f'The factorial of {value} is: ', fact)  # Muestra el resultado final
    else:
        print("Please, enter a positive integer number")  # Mensaje si no cumple la condición

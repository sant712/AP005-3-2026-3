for i in range(1,6):            # Bucle externo que toma valores del 1 al 5
    while i <= 4:               # Bucle interno que opera mientras 'i' sea menor o igual a 4
        i += 1                  # Incrementa el valor de 'i' en 1
        print(i)                # Imprime el valor actualizado de 'i'
    break                       # Rompe y finaliza el bucle externo inmediatamente en la primera vuelta completa

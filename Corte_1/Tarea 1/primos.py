import time
inicio = time.time()            # Guarda el marcador de tiempo inicial para medir rendimiento

for i in range(0,31):           # Itera desde el número 0 hasta el 30
    conta = 0                   # Inicializa el contador de divisores en 0 para cada número
    for n in range(1, i+1):     # Comprueba todos los posibles divisores desde 1 hasta 'i'
        residue = i%n           # Obtiene el residuo de la división
        if residue == 0:        # Si es divisor exacto...
            conta = conta + 1   # Aumenta el contador de divisores
              
    if conta == 2:              # Un número primo solo tiene exactamente 2 divisores (1 y sí mismo)
        print(f'{i} es un primo')
        
fin = time.time()               # Guarda el marcador de tiempo final
print("t = ", (fin - inicio)*1000)  # Muestra el tiempo transcurrido en milisegundos

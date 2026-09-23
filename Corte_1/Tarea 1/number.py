import random                   # Importa funciones para generar números aleatorios
from matplotlib import pyplot as plt  # Importa la librería para crear gráficos

numbers_a = range(1, 13)        # Define el eje X con 12 puntos (meses o secuencia)
numbers_b = [random.randint(1, 1000) for i in range(12)]  # Crea 12 números aleatorios entre 1 y 1000 para el eje Y
plt.plot(numbers_a, numbers_b)  # Dibuja la gráfica de líneas con los datos dados
plt.show()                      # Muestra la ventana con el gráfico generado

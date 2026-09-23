# 9) Imprimir primos sin optimización (revisa todos los divisores siempre)
tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1

# 10) Versión optimizada con break (detiene el bucle interno al hallar un divisor)
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break               # Rompe el bucle interno inmediatamente al saber que no es primo
    if (primo):
        print(n)
    else:
        primo = True
    n += 1

# 11) Conteo de ciclos para medir la mejora porcentual
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1   # Cuenta cada iteración de la prueba sin break
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1   # Cuenta cada iteración de la prueba con break
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')

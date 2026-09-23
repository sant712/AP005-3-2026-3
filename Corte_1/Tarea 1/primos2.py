a = 1                           # Inicializa la variable de control del bucle en 1
value = input('Ingrese un valor')  # Pide un límite superior al usuario
value = int(value)              # Convierte el valor ingresado a entero

while a == 1:                   # El bucle se repite mientras 'a' sea igual a 1
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
            
            # Líneas comentadas de depuración para rastrear variables paso a paso
            # print("i = ", i)
            # print("n = ", n)
            # print("residue = ", residue)
            # print("conta = ", conta)
    if conta == 2:
       print(f'{i} es un primo')
       print("\n")
    else:
       print(f'{i} NOOO es un primo')
       print("\n")

    print('Do you want to continue?. Press 1 to do that')
    a = input()                 # Lee la decisión del usuario para continuar
    a = int(a)

    if a != 1:
        break                   # Rompe el bucle principal si el usuario ingresa algo diferente de 1

    value = input('Ingrese un valor')  # Pide un nuevo valor si decide continuar
    value = int(value)

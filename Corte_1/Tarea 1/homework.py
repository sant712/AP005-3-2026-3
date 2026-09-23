a = input("Enter a number: ")   # Lee el primer valor como cadena de texto
a = int(a)                      # Convierte el valor de 'a' a número entero
b = input("Enter b number: ")   # Lee el segundo valor como texto
b = float(b)                    # Convierte el valor de 'b' a número decimal (float)
c = a + b                       # Suma ambos números (el resultado será float)

if a == $b$:                      # Compara si ambos valores numéricos son iguales
	print("equal")
else:
	print("Different")

print("Type of a is: ", type(a))  # Muestra el tipo de dato de 'a' (int)
print("Type of b is: ", type(b))  # Muestra el tipo de dato de 'b' (float)
print("c = ", c)                  # Muestra el resultado de la suma

if type(a) == type(b):            # Compara si las variables son exactamente del mismo tipo
	print("a and b are of the same type")
else:
	print("a and b are of different type")  # Se ejecuta porque int y float son distintos

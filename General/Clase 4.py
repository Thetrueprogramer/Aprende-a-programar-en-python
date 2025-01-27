# Bienvenido a la 3ra clase del curso de Python, hoy aprenderemos sobre los bucles.

# Ejemplo 1: Usar 'range()' para generar una secuencia de números
for i in range(5):
    print("Número:", i)

# Ejemplo 2: Bucle 'while' para contar hasta 5
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# Ejemplo 3: Usar 'break' para salir del bucle
for i in range(10):
    if i == 5:
        break
    print(i)

# Ejemplo 4: Usar 'continue' para saltar una iteración
for i in range(5):
    if i == 2:
        continue
    print(i)

# Ejemplo 5: Bucle 'while' con una condición de salida
intento = 0
while intento < 3:
    print("Intento número:", intento)
    intento += 1

# Los espero en la proxima clase
# Usa 'for' para iterar sobre rangos de números y 'while' para repetir mientras se cumpla una condición.

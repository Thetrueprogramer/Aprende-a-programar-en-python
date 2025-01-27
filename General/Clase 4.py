# Bienvenido a la 4ta clase del curso de Python, hoy aprenderemos sobre los bucles.
# Te enseñaré con un ejemplo práctico.

# Ejemplo 1: Bucle 'for' para iterar sobre una lista

# Definimos una lista de frutas
frutas = ["manzana", "banana", "cereza"]
# Usamos un bucle 'for' para recorrer cada fruta en la lista
for fruta in frutas:
    # Imprimimos el nombre de cada fruta
    print(fruta)

# Ejemplo 2: Usar 'range()' para generar una secuencia de números

# Usamos range() para generar números del 0 al 4
for i in range(5):
    # Imprimimos el número actual
    print("Número:", i)

# Ejemplo 3: Bucle 'while' para contar hasta 5

# Inicializamos una variable contador en 0
contador = 0
# Usamos un bucle 'while' que se ejecutará mientras el contador sea menor que 5
while contador < 5:
    # Imprimimos el valor actual del contador
    print("Contador:", contador)
    # Incrementamos el contador en 1 en cada iteración
    contador += 1

# Ejemplo 4: Usar 'break' para salir del bucle

# Usamos un bucle 'for' para recorrer los números del 0 al 9
for i in range(10):
    # Si el número es 5, salimos del bucle
    if i == 5:
        break
    # Imprimimos el número actual
    print(i)

# Ejemplo 5: Usar 'continue' para saltar una iteración

# Usamos un bucle 'for' para recorrer los números del 0 al 4
for i in range(5):
    # Si el número es 2, saltamos esta iteración y continuamos con la siguiente
    if i == 2:
        continue
    # Imprimimos el número actual
    print(i)

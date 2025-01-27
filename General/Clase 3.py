# Bienvenido a la 3ra clase del curso de python hoy aprenderemos sobre los condicionales
# Te enseñare con un ejemplo

# Pedir al usuario que ingrese un número
numero = float(input("Ingresa un número: "))
# La función float convierte entradas de texto en entradas de punto flotante (punto decimal) y la función input recibe una entrada del usuario
# Usar condicionales para determinar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Usamos if para preguntar si la condición que especificaremos después del if es correcta en este caso que el número es mayor a cero
# Usamos elif para cuando la condición del if es incorrecta
# Lo que hacemos aquí es decirle al sistema que si la condición de arriba no es correcta
# Le damos otra condición en este caso que el número sea menor a cero, o sea, negativo
# Y usamos else para cuando la condición de if es incorrecta y no queremos poner otra condición
# En este caso si ambas condiciones son incorrectas significa que el número es cero

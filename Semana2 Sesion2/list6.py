"""Convertir a Mayusculas"""

texto = "Mi novio es el mejor del mundo"
print(texto)

texto_mayusculas = texto.upper()
print(texto_mayusculas)

#convertir a minusculas
texto2 = "ME QUIERO CASAR CON VOS"
print(texto2)
texto2_minusculas = texto2.lower()
print(texto2_minusculas)

#convertir a mayusculas la primera letra
nombre = "steven sequeira"
print(nombre)
nombre_minuscula = nombre.capitalize()
print(nombre_minuscula)

#Convertir la primera letra de cada palabra a mayuscula
nombre2 = "gabriela guerrero"
print(nombre2)

nombre2_mayuscula = nombre2.title()
print(nombre2_mayuscula)

#Reemplazar texto

texto = "Hola mi vida pookie"
print(texto)

texto_reemplazado = texto.replace("mi vida", "mi amor")
print(texto_reemplazado)

#Eliminar espacios en blanco
texto = "Hola mi vida pookie"
print(texto)
texto_sin_espacios = texto.strip()
print(texto_sin_espacios)

#Formato numero
numero = 15000000000
print(numero)
numero_formato = "{:,}".format(numero)
print(numero_formato)

#Formato decimal
numero_decimal = 1500.50
print(numero_decimal)
numero_formato = "{:.2f}".format(numero_decimal)
print(numero_formato)


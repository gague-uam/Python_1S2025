"""Concatenacion de cadenas"""

nombre = "Steven :3" 
apellido = "Sequeira ><"

nombre_completo = nombre + " " + apellido
print(nombre_completo)

nombre_C = f"{nombre} {apellido}"
print(nombre_C)

#concatenar
nombreCompleto = " ".join([nombre, apellido])
print(nombreCompleto)

#lista y concatenar

lista = []
lista.append(nombre)
lista.append(apellido)
nombreCompleto = " ".join(lista)
print(nombreCompleto)

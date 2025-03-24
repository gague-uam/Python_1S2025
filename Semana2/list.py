#Almacenar 10 numeros enteros

list_int = list()

for i in range(10):
    list_int.append(int(input(f"{i+1} out of 10 - Enter a number: ")))

print(list_int)
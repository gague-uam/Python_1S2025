#Agregar los nombres de x cantidad de estudiantes

list_students = list()

def add_student():
    student = input("Enter a name:")
    list_students.append(student)

def show_students():
    print("List of students: ")
    for student in list_students:
        print(student)

while True:
    add_student()
    show_students()
    if input("Do you want to add another student? (y/n): ").lower() != "y":
        break

print("Thanks for using the program")
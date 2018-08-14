students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        stdents_titlecase = student.title()
    return students_titlecase 

def print_students_titlecase():
    students_titlecase = []
    for student in students:
        stdents_titlecase = student.title()
    print(students_titlecase) 

def add_student(name):
    students.append(name)

students_list = get_students_titlecase()

add_student("shaheela")

print_students_titlecase()

print("this is out from get", students_list)
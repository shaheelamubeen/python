students = []

def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student.title()
        return students_titlecase

def print_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student.title()
        print(students_titlecase)

def add_student(name):
    students.append(name)

students_list = get_students_titlecase()

add_student("shaheela")

print_students_titlecase()

print("this is out from get",students_list)


@@@adding title,student_id,list and dictionary

students = []

def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student["name"].title()
        return students_titlecase

def print_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student["name"].title()
        print(students_titlecase)

def add_student(name, student_id):
    student = {"name":name, "student_id":student_id}
    students.append(student)

#students_list = get_students_titlecase()

add_student(student=10,name="shaheela")
print(students)
print_students_titlecase()

#print("this is out from get",students_list)



@@@ARGS
students = []

def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student["name"].title()
        return students_titlecase

def print_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student["name"].title()
        print(students_titlecase)

def add_student(name, student_id):
    student = {"name":name, "student_id":student_id}
    students.append(student)

def with_args(name, *args):
    print(name)
    print(args)

#students_list = get_students_titlecase()

#add_student(student=10,name="shaheela")
#print(students)
#print_students_titlecase()

#print("this is out from get",students_list)

with_args("shaheela","loves python", 57, None, "hi")

o/p:-
shaheelas-MacBook-Air:python shaheelamubeen$ python fivefunctions.py
shaheela
('loves python', 57, None, 'hi')

@@@kwargs

students = []

def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student["name"].title()
        return students_titlecase

def print_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase = student["name"].title()
        print(students_titlecase)

def add_student(name, student_id):
    student = {"name":name, "student_id":student_id}
    students.append(student)

def with_args(name, *args):
    print(name)
    print(args)

def with_kwargs(name, **kwargs):
    print(name)
    print(kwargs)
    print(kwargs["city"], kwargs["country"])
#students_list = get_students_titlecase()

#add_student(student=10,name="shaheela")
#print(students)
#print_students_titlecase()

#print("this is out from get",students_list)

with_args("shaheela","loves python", 57, None, "hi")

with_kwargs("aakash", city="london", country="UK")


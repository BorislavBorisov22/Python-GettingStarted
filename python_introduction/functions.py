students = []


def get_students_title_case():
    students_title_case = []
    for student in students:
        students_title_case.append(student['name'].title())
    return students_title_case


def print_students_titlecase():
    students_title_case = get_students_title_case()
    print(students_title_case)


def add_student(name, id):
    student = {"name": name, "id": id}
    students.append(student)


def var_args(name, *args):
    print(args)


def var_kwargs(name, **kwargs):
    print(kwargs)


add_student(name='ivan', id=33)
print_students_titlecase()

var_args('somename', 1, 2, 3, True)
var_kwargs('somename', description="Learning Python", cool=True)

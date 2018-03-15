students = []


def get_students_title_case():
    students_title_case = []
    for student in students:
        students_title_case.append(student.title())
    return students_title_case


def print_students_titlecase():
    students_title_case = get_students_title_case()
    print(students_title_case)


def add_student(student):
    students.append(student)
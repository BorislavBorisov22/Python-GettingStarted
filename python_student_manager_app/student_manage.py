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


student_name = input('Enter student name: ')
student_id = input('Enter student id: ')

# print(student_name)
# print(student_id)
# add_student(student_name, student_id)
# print_students_titlecase()
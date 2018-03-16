students = []


class Student:

    school_name = 'Springfield Elementary'

    def __init__(self, name, id=1):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


# mark = Student('ivan')
# print(mark.get_name_capitalize())

print(Student.school_name)
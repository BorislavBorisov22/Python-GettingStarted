from student import Student


class HighSchoolStudent(Student):

    school_name = 'SpringField HighSchool'

    def get_school_name(self):
        return 'This is a highschool student'

    def get_name_capitalize(self):
        return super().get_name_capitalize() + ' in highschool'
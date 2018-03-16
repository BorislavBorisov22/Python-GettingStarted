def getIterator():
    students = ['Mark', 'Henry']

    def iterate():
        for student in students:
            print(student)

    return iterate


iterator = getIterator()
iterator()
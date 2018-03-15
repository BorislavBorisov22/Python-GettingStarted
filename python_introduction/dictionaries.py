student = {"name": 'Mark', "student_id": 15163, "feedback": None}

print(student['name'] == 'Mark')
print(student.get('non_existing_property', 'Unknown'))

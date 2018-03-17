from hs_student import HighSchoolStudent
from student import Student

from flask import redirect, render_template, Flask, url_for, request

students = []

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student_id", "")
        new_student_name = request.form.get("student_name", "")
        new_student = Student(new_student_name, new_student_id)
        students.append(new_student)

        return redirect(url_for('students_page'))
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
number = 5
if number == 5:
    print('Number is five')
else:
    print('Number is {0}'.format(number))

is_java_course = False
python_course = False

if python_course or (not is_java_course):
    print('It is a python course')

# ternary if
a = 1
b = 2
print('bigger' if a > b else 'smaller')
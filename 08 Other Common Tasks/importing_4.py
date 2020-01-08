from importing_3 import teacher_comment_with_grade
students = {'Tony': 95, 'Betsy': 85, 'Peter': 75}

for student in students:
    print(teacher_comment_with_grade(students[student], student))

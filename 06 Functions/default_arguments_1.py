def teacher_comment(test_score, student_name):
    """
    This function takes an <int> test score and returns a teacher comment based on the score.
    Optional Student Name <str> to be added to the comment

    Returns a string teacher comment
    """
    if test_score > 90:
        return 'Great Job ' + student_name
    elif test_score > 80:
        return 'Pretty good ' + student_name
    else:
        return 'You could do better ' + student_name


students = {'Tony': 95, 'Betsy': 85, 'Peter': 75}

for student in students:
    score = students[student]
    comment = teacher_comment(score, student)
    print(score, '-->', comment)

no_name = teacher_comment(40)
print('No Name 40 -->', no_name)

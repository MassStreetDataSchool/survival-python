test_scores = [95, 85, 75]

for test_score in test_scores:
    if test_score > 90:
        teacher_comment = 'Great Job'
    elif test_score > 80:
        teacher_comment = 'Pretty good'
    else:
        teacher_comment = 'You could do better'

    print(teacher_comment)



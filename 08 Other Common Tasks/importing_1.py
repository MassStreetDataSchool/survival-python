def teacher_comment(test_score, student_name=''):
    """
    This function takes an <int> test score and returns a
    teacher comment based on the score.

    Returns a string teacher comment
    """
    if test_score > 90:
        return 'Great Job ' + student_name
    elif test_score > 80:
        return 'Pretty good ' + student_name
    else:
        return 'You could do better ' + student_name


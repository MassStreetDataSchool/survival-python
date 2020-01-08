def teacher_comment(test_score):
    """
    This function takes an <int> test score and returns a teacher comment based on the score.

    Returns a string teacher comment
    """
    if test_score > 90:
        return 'Great Job'
    elif test_score > 80:
        return 'Pretty good'
    else:
        return 'You could do better'
    print('Bottom of the function, wont get here')


for score in [95, 85, 75]:
    comment = teacher_comment(score)
    print(score, '-->', comment)

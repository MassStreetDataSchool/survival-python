def first_last(full_name):
    first_name = ''
    last_name = ''
    has_been_a_space = False
    for letter in full_name:
        if letter == ' ':
            has_been_a_space = True
        elif has_been_a_space:
            last_name = last_name + letter
        else:
            first_name = first_name + letter

    print('First: ', first_name)
    print('Last: ', last_name)


first_last('Tony Macaroni')

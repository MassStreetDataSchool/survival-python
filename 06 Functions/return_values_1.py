def make_full_name(first, last):
    """
    This function takes two arguments: first and last, which represent a person's first name and last name respectively

    Returns a single string '<first name> <space> <last name>'
    """
    full_name = first + ' ' + last
    return full_name


full = make_full_name('Tony', 'Macaroni')
print(full)

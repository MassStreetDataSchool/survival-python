def can_create_a_Fibonacci_number(int_1, int_2):
    """
    This function checks to see if the sum, difference, product, or module
     of the two inputs product a Fibonacci number.

    1, 1, 2, 3, 5, 8, 13, 21, 34 ...

    The two inputs are assumed to be integers
    """
    sum = int_1 + int_2
    product = int_1 * int_2
    if int_1 > int_2:
        diff = int_1 - int_2
        mod = int_1 % int_2
    else:
        diff = int_2 - int_1
        mod = int_1 % int_2

    possible_fibs = [sum, product, diff, mod]

    fib1 = 1
    fib2 = 2
    fib_found = False

    while fib2 < max(possible_fibs) and not fib_found:
        new_fib = fib1 + fib2
        if new_fib in possible_fibs:
            fib_found = True
            if new_fib == sum:
                print('Sum creates: ', new_fib)
            elif new_fib == product:
                print('Product creates: ', new_fib)
            elif new_fib == diff:
                print('Difference creates: ', new_fib)
            else:
                print('Modulo creates: ', new_fib)
        fib1 = fib2
        fib2 = new_fib

    if not fib_found:
        print('No Fibonacci Number found under: ', fib2)


can_create_a_Fibonacci_number(30, 33)
can_create_a_Fibonacci_number(30, 4)
can_create_a_Fibonacci_number(29, 4)

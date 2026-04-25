def euclidean_algorithm():
    '''Prints the greatest common factor between two numbers.'''
    # Get user integers.
    while True:
        try:
            a, b = int(input('Enter the first integer: ')), int(input('Enter the second integer: '))
            break
        except ValueError:
            print('Invalid integers were provided.\n')

    print()
    dividend = a
    divisor = b

    # Take absolute values for the greatest factor.
    if dividend < 0:
        dividend = -dividend

    if divisor < 0:
        disvisor = -divisor

    # Set the dividend to be greater than the divisor.
    if dividend < divisor:
        dividend, divisor = divisor, dividend

    # Stop when the initial divisor or remainder is zero.
    last_divisor = dividend

    while divisor != 0:
        remainder = dividend % divisor
        print(f'Remainder of {dividend} and {divisor}: {remainder}')

        last_divisor = divisor
        print(f'New divisor: {last_divisor}')

        dividend, divisor = divisor, remainder
        print(f'New dividend and divisor: {dividend}, {divisor}')

    # Return the last divisor.
    print(f'\nThe GCF of {a} and {b} is {last_divisor}.')
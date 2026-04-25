def prompt_user_character(message, chars=tuple(), allow_invalid=True):
    '''Prompts the user for a character.
    Args:
        message: The message to display.
        chars: The available characters to input.
        allow_invalid: Whether or not invalid characters are accepted.
    returns:
        string: A string containing a trimmed, uppercase character.
    '''
    ch = ''

    while True:
        ch = input(f'\n{message}').strip().upper()

        if ch in chars or allow_invalid:
            return ch

        print('\nInvalid character.')

def handle_options(header, options, allow_invalid, **addtl_funcs):
    '''Handles menu options.
    Args:
        header: The name of the menu.
        options: A dictionary mapping characters and their labels to functions and their parameters, if any.
        allow_invalid: Whether or not error messages should be output for unsupported options
        addtl_funcs: Any additional function that must be performed as part of the menu display mapped to their parameters (in a container).'''
    while True:
        print(header)
        
        # Execute additional functions.
        for func, info in addtl_funcs.items():
            info[0](*info[1])

        # Display options.
        for option in options:
            print(f'\t({option[0]}) {option[1]}')

        # Check selection and execute the corresponding function.
        ch = prompt_user_character(f'Enter a character{', or anything else to go back' if allow_invalid else ''}: ', [option[0] for option in options], allow_invalid)
        print()

        for option, info in options.items():
            if ch == option[0]:
                info[0](*info[1])
                break
        else:
            if allow_invalid:
                break
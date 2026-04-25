def delete_set(dict, display_func, type):
    '''Allows the user to delete an existing set.
    Args:
        dict: The dictionary from which to choose the set.
        display_func: How to display the dictionary.
        type: The string representing the set.'''
    print(f'\n[{type.upper()} DELETION]')
    # Check if sets exist.
    if not dict:
        print(f'No {type} to delete.')
        return

    # Prompt user for a set.
    display_func()
    print()
    name = prompt_element(f'Select a {type} to delete', f'This {type} does not exist.', dict, True)
    
    # Confirm with user.
    confirm = prompt_user_character(f'\nAre you sure you want to delete "{name}" (Y/N)? ', ('Y', 'N'), False)
    
    if confirm == 'Y':
        del dict[name]
        print(f'\nDeleted "{name}".')
    else:
        print(f'\n"{name}" was not deleted.')

def prompt_element(prompt, message, to_check, should_exist):
    '''Prompts the user for an element of a set.
    Args:
        prompt: The prompt.
        message: A message that is output when the condition is not satisfied.
        to_check: The set to check.
        should_exist: Whether the condition should be satisfied when the element exists.
    Returns:
        string: The element.'''
    while True:
        element = input(f'{prompt}: ')

        if not check_element(to_check, element, should_exist):
            print(f'\n{message}', end=' ')
        else:
            return element

def check_element(to_check, element, should_exist):
    '''Checks whether an element satisfies the conditions.
    Args:
        to_check: The set to check.
        element: The element in question.
        should_exist: Whether or not the element should exist.
    Returns:
        boolean: Whether or not the element is satisfactory.'''
    satisfied = True

    if should_exist:
        if element not in to_check:
            satisfied = False
    else:
        if element in to_check:
            satisfied = False

    return satisfied

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
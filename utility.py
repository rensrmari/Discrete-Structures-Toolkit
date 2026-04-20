def prompt_user_character(message):
    '''Prompts the user for a character.
    Args:
        message: The message to display.
    returns:
        string: A string containing a trimmed, uppercase character.
    '''
    return input(f'\n{message}').strip().upper()
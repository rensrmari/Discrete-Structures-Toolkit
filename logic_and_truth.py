import math
import re
import utility

def replace_substrings(exp, dict):
    '''Replaces an expression according to a supplied dictionary.
    Args:
        exp: The expression to use.
        dict: The dictionary of strings mapped to their replacements.
    Returns:
        string: A modified expression.'''
    
    for original, replacement in dict.items():
        exp = re.compile(original, re.IGNORECASE).sub(replacement, exp)

    return exp

def increment_binary(str, length):
    '''Increments a string representing a binary number.
    Args:
        str: The string to change.
        length: The desired length of the binary number.
    Returns:
        string: A binary number as a string with a certain length.'''
    # Convert binary string to integer and add one.
    num = int(str, 2) + 1

    # Convert integer back to binary string without prefix.
    str = bin(num)[2:]

    # Maintain length of binary string.
    while len(str) < length:
        str = '0' + str

    return str

def update_table_col(dict, key, val):
    '''Updates a table with column values.
    Args:
        dict: A table to modify.
        key: The key of the column.
        val: The value to append to the column.'''
    
    dict.setdefault(key, [])
    dict[key].append(val)

def print_bar(width):
    '''Prints a bar at a specificed width.
    Args:
        width: The width of the bar.'''
    print('-' * width)

def print_cell(str, length, boolean=False):
    '''Prints a cell as a continuation of a previous cell.
    Args:
        str: A string to print.
        length: The length of the column's string.
        boolean: Whether or not the string represents a boolean.
    '''
    if boolean:
        if str == False:
            str = 'F'
        else:
            str = 'T'

    spacing = (length - len(str)) / 2
    left_spacing = math.floor(spacing)
    right_spacing = math.ceil(spacing)

    left_padding = len(str) + left_spacing
    right_padding = left_padding + right_spacing
    right_padding += length - (left_spacing + len(str) + right_spacing)

    print(f' {str.rjust(left_padding).ljust(right_padding)} |', end='')

def replace_variables(exp, name, dict):
    '''Replaces variables of an expression sequentially for evaluation.
    Args:
        exp: The expression to use.
        name: The name of the dictionary.
        dict: The dictionary whose keys will be replaced with their values.
    Returns:
        string: A modified expression.'''
    for key in dict:
        # Locate the variable by itself.
        pattern = re.compile(rf'\b{key}\b')
        exp = pattern.sub(f'{name}[\'{key}\']', exp)
    return exp

def prompt_user_exp(message):
    '''Prompts the user for a valid expression.
    Args:
        message: A prompt.
    Returns:
        Proposition: A valid expression.'''
    prop = Proposition()
    user_exp = input(message)

    while not prop.set_expression(user_exp):
        user_exp = input(f'\nInvalid input. {message}', end='')

    return prop

def print_changes(orig_exp, new_exp, to_print, message):
    '''Prints any changes to expressions.
    Args:
        orig_exp: The original expression.
        new_exp: The new expression.
        to_print: Whether or not the change should be printed.
        message: A message to accompany the displayed change.'''
    
    if to_print:
        prop = Proposition()
        prop.set_expression(new_exp)
        
        if new_exp != orig_exp:
            print(f'\n{message}')
            print(f'New Statement: {prop.get_display_exp()}')

def simplify_conditionals(exp, bi, to_print=False):
    '''Converts biconditionals to conditionals, or conditionals to their disjunction form.
    Args:
        exp: The string containing the used expression.
        bi: Whether or not the supplied expression contains biconditionals.
        to_print: Whether or not the process should be printed.
    Returns:
        string: The modified expression.'''
    orig_exp = exp
    pattern = re.compile(r'(\(.*\)|[^ (]+) (iff|IFF) (\(.*\)|[^ (]+)') if bi else re.compile(r'(\(.*\)|[^ (]+) (implies|IMPLIES)')
    exp = pattern.sub(r'(\1 implies \3) and (\3 implies \1)' if bi else r'not \1 or', exp)
    
    print_changes(orig_exp, exp, to_print, f'Simplifying {'bi' if bi else ''}conditionals...')
    return exp

def simplify_negations(exp, to_print=False):
    '''Simplifies negations by distributing them and cancelling duplicates.
    Args:
        exp: The expression to use.
        to_print: Whether or not the process should be printed.
    Returns:
        string: The modified expression.'''
    
    while True:
        orig_exp = exp

        # Look for substrings that need to distribute a not or duplicate nots.
        dist = re.compile(r'not\s*\((.*)\)')
        dist_matches = dist.findall(exp)

        dup = re.compile(r'not not')
        dup_matches = dup.findall(exp)
        
        if not dist_matches and not dup_matches:
            break

        # Distribute the negation and invert any conjunctions or disjunctions.
        exp = dist.sub(r'\1', exp)

        for match in dist_matches:
            inside = match.strip()
            words = inside.split(' ')
            new_words = []

            for word in words:
                if word == 'and':
                    new_words.append('or')
                elif word == 'or':
                    new_words.append('and')
                else:
                    new_words.append(f'not {word}')

            for i, new_word in enumerate(new_words):
                exp = exp.replace(words[i], new_word, 1)

        # Eliminate duplicate nots.
        exp = dup.sub('', exp)
        print_changes(orig_exp, exp, to_print, 'Simplifying negations...')
    
    return exp

def create_truth_table():
    print('\n[TRUTH TABLE]')

    # Prompt user for expression.
    prop = prompt_user_exp('Please enter a statement: ')

    # Create and display truth table.
    table = TruthTable(prop)
    table.print_table()
    utility.prompt_user_character('Enter anything to go back: ')

def create_deduction():
    print('\n[DEDUCTION RULE]')

    # Prompt user for two expressions and a deduction.
    prop1, prop2, deduction = prompt_user_exp('Please enter the first statement: '), \
                                prompt_user_exp('Please enter the second statement: '), \
                                prompt_user_exp('Please enter a deduction: ')

    # Check if the deduction only uses existing variables.
    vars = list(prop1.get_vars().keys()) + list(prop2.get_vars().keys())
    for deduct_var in list(deduction.get_vars().keys()):
        if deduct_var not in vars:
            print('\nDeduction rule should not contain new variables.')
            break
    else:
        # Combine expressions in a truth table.
        table = TruthTable(prop1)
        table.extend(prop2)
        table.extend(deduction)
        table.print_table()

        # Iterate through rows of each column and determine if the expressions are true in the same rows.
        valid_rule = True
        for i in range(table.column_size):
            truth_prop1 = table.get_table()[prop1.get_display_exp()][i]
            truth_prop2 = table.get_table()[prop2.get_display_exp()][i]
            truth_deduction = table.get_table()[deduction.get_display_exp()][i]

            if truth_prop1 and truth_prop2 and not truth_deduction: # Premises are true but conclusion is not
                valid_rule = False
                break
        
        if valid_rule:
            print('\nValid deduction rule!')
        else:
            print('\nDeduction rule does not work.')

def break_statement():
    print('\n[STATEMENT SIMPLIFICATION]')

    # Prompt user for expression.
    prop = prompt_user_exp('Please enter a statement: ')
    print(f'\nStatement: {prop.get_display_exp()}')

    # Break down biconditionals and conditionals.
    prop.set_expression(simplify_conditionals(prop.get_expression(), True, True))
    prop.set_expression(simplify_conditionals(prop.get_expression(), False, True))

    # Simplify negations.
    prop.set_expression(simplify_negations(prop.get_expression(), True))

    print('\nStatement has been broken down fully.')
    utility.prompt_user_character('Enter anything to go back: ')

class Proposition:
    def __init__(self):
        self.exp = ''
        self.display_exp = ''
        self.eval_exp = ''
        self.vars = {
            'name': "self.vars['vars']",
            'vars': {}
        }

    def set_expression(self, exp):
        '''Assigns a new expression to the object and reads its variables.
        Args:
            exp: The expression to assign.
            dict: The dictionary whose keys will correspond to the variables.
        Returns:
            boolean: Whether or not the expression was a valid proposition.'''
        self.exp = exp

        # Get the display expression.
        operators = {
            'xor': '⊕',
            'and': '∧',
            'or': '∨',
            'not': '¬',
            'implies': '→',
            'iff': '↔'
        }

        # Replace operators and remove spaces to the right of negation symbols.
        display_exp = replace_substrings(exp, operators)
        pattern = re.compile(r'¬\s+')
        display_exp = pattern.sub(r'¬', display_exp)
        self.display_exp = display_exp

        # Replace expression operators.
        operators = {
            'xor': '^',
            'and': 'and',
            'or': 'or',
            'not': 'not'
        }

        exp = replace_substrings(exp, operators)

        # Replace biconditionals and conditionals.
        exp = simplify_conditionals(exp, True)
        exp = simplify_conditionals(exp, False)
    
        # Get variables, ignoring parentheses, spaces, and operators.
        words = exp.split(' ')
        pattern = re.compile(r'[^ ()]+')
        ignored_operators = {}
        for operator in operators:
            ignored_operators[operator] = ''

        for word in words:
            word = replace_substrings(word, ignored_operators)
            match = pattern.search(word)
            if word and match:
                self.vars['vars'][match.group()] = 0

        # Replace variables in expression with dictionary accesses and check for valid expression.
        exp = replace_variables(exp, self.vars['name'], self.vars['vars'])
        self.eval_exp = exp

        try:
            self.eval_expression()
        except:
            return False
        
        return True
    
    def get_expression(self):
        '''Gets the original expression of the proposition.
        Returns:
            string: The original expression.'''
        return self.exp
    
    def eval_expression(self):
        '''Evaluates its expression.
        Returns:
            boolean: The truth value of the expression given the current state of its variables.'''
        return bool(eval(self.eval_exp))

    def get_display_exp(self):
        '''Gets the display representation of the expression.
        Returns:
            string: An expression containing propositional symbols.'''
        return self.display_exp
    
    def get_vars(self):
        '''Gets the proposition's variables
        Returns:
            dictionary: Variables mapped to values.'''
        return self.vars['vars']

    def update_vars_binary(self, str):
        '''Updates the values of variables according to a binary string.
        Args:
            str: The binary string to use.'''
        for i, key in enumerate(self.get_vars().keys()):
            self.vars['vars'][key] = int(str[i])

    def update_vars_dict(self, keys, new_vals):
        '''Updates the values of variables according to a dictionary.
        Args:
            keys: A list containing the keys to update.
            new_vals: The dictionary containing the keys mapped to their new values.'''
        for key in keys:
            self.vars['vars'][key] = new_vals[key]

class TruthTable:
    def __init__(self, exp):
        self.exp = exp
        self.table, self.column_size = self.generate_table(exp)

    def generate_table(self, exp):
        '''Creates a dictionary of propositional variables mapped to their truth values.
        Returns:
            (dictionary, int): A dictionary containing variables to a list of truth values, and the number of truth values.'''
        # Get symbolic representation of expression as well as variables.
        table = {}
        display_exp = exp.get_display_exp()
        vars = exp.get_vars()
        
        # Process boolean values using a binary string to store each permutation of inputs.
        count = 0
        final_val = 2 ** len(vars)
        current_binary = '0' * len(vars)

        while count < final_val:
            # Assign truth values as binary digits to their variables.
            for i, col in enumerate(vars):
                update_table_col(table, col, True if current_binary[i] == '1' else False)

            update_table_col(table, display_exp, exp.eval_expression())

            # Increment binary.
            current_binary = increment_binary(current_binary, len(vars))
            exp.update_vars_binary(current_binary)
            count += 1
        
        return (table, final_val)
    
    def get_table(self):
        '''Gets the table dictionary.
        Returns:
            dictionary: A dictionary of variables mapped to lists of truth values.'''
        return self.table

    def extend(self, exp):
        '''Extends the table with columns dependent on existing variables.
        Args:
            exp: The Proposition for the new column.'''
        # Get the truth values of only the variables included in the expression.
        truth_values = []

        for i in range(self.column_size):
            row = {}

            for var in exp.get_vars().keys():
                row[var] = self.table[var][i]
            
            truth_values.append(row)

        # Evaluate each row of truth values using the additional expression.
        for row in truth_values:
            exp.update_vars_dict(exp.get_vars().keys(), row)
            value = exp.eval_expression()
            update_table_col(self.table, exp.get_display_exp(), value)

    def print_table(self):
        '''Displays a truth table for an expression.'''
        # Display table header.
        add_chars = 0
        for input in self.table:
            add_chars += len(input) + 3
        width = 1 + add_chars

        print('Truth Table:')
        print_bar(width)
        print('|', end='')
        for input in self.table:
            print_cell(str(input), len(input))
        print()
        print_bar(width)

        # Iterate through each variables truth values.
        for i in range(self.column_size):
            print('|', end='')
            
            for input in self.table:
                print_cell(self.table[input][i], len(input), True)

            print()
            print_bar(width)
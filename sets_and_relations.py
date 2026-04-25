import utility

user_sets = {}
user_rels = {}

def print_set(name, user_set):
    '''Prints a given set.
    Args:
        user_set: The set to print.'''
    
    print(f'{name}: ', end='{ ')

    if len(user_set) > 0:
        temp_list = list(user_set)
        print(f'{temp_list[0]}', end='')

        for i in range(1, len(temp_list)):
            print(f', {temp_list[i]}', end='')

    print(' }')

def display_sets():
    '''Displays the user's sets.'''
    print(f'{'User Sets'}: {'None' if not user_sets else ''}')

    for name, user_set in user_sets.items():
        print_set(name, user_set)

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

def add_element_set(user_set):
    '''Adds an element to a set.
    Args:
        user_set: The set to update.'''
    user_element = prompt_element('Enter an element', 'Element already exists.', user_set, False)
    user_set.add(user_element)
    print(f'{user_element} added.\n')

def remove_element_set(user_set):
    '''Removes an element from a set.
    Args:
        user_set: The set to update.'''

    # Make sure there are still elements in the set.
    if len(user_set) == 0:
        print('No more elements to remove.')
        return
    
    user_element = prompt_element('Enter an element', 'Element does not exist.', user_set, True)
    user_set.remove(user_element)

def create_set(dict, dict_name, new_set):
    '''After the elements of a set have been decided, finish the process of saving the set to the dictionary.
    Args:
        dict: Where the set should be saved.
        dict_name: How to refer to the set.
        new_set: The set to be saved.
    Returns:
        str: The name of the set.'''
    name = prompt_element(f'Enter a unique name for {dict_name}', 'This name is already taken.', dict, False)
    dict[name] = new_set
    print(f'\n"{name}" successfully saved!')
    return name

def build_new_set():
    '''Allows the user to create a new set and save it to user_sets.
    Returns:
        tuple: A tuple containing the name of the set and the set itself.'''
    print('[SET CREATION]')
    new_set = set()

    # Prompt user for number of elements.
    while True:
        user_num = input('Enter the number of elements to add: ')

        try:
            user_num = int(user_num)
            break
        except:
            print('\nInvalid input. ', end='')
        
    # Read all elements, one by one.
    for i in range(user_num):
        add_element_set(new_set)
        print_set(f'Current Set', new_set)

    # Prompt user for a name and save the set.
    print()
    return (create_set(user_sets, 'this set', new_set), new_set)

def edit_set(type, dict, print_func, display_func, add_func, remove_func):
    '''Allows the user to select a set and modify its elements.
    Args:
        type: The string representing the set or relation.
        dict: The dictionary containing the sets.
        print_func: The function to print the set.
        display_func: The function to display all sets.
        add_func: The function to add an element.
        remove_func: The function to remove an element. '''
    
    print('\n[SET EDITOR]')

    # Check if sets exist.
    if not dict:
        print(f'No {type} to edit.')
        return

    # Prompt user for a set.
    display_func()
    name = prompt_element(f'Select an existing {type} to edit', f'This {type} does not exist.', dict, True)
    user_set = dict[name]

    # New menu for editing.
    options = {
        ('A', 'Add an Element'): (add_func, (user_set,)),
        ('R', 'Remove an Element'): (remove_func, (user_set,))
    }

    utility.handle_options(f'\n[{type.upper()} EDITOR]', options, True, print_func=(print_func, (name, user_set)))

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
    confirm = utility.prompt_user_character(f'\nAre you sure you want to delete "{name}" (Y/N)? ', ('Y', 'N'), False)
    
    if confirm == 'Y':
        del dict[name]
        print(f'\nDeleted "{name}".')
    else:
        print(f'\n"{name}" was not deleted.')

def operate_given(op):
    '''Creates a new set from a set operation.
    Args:
        op: A string representing the operation to perform.'''
    print(f'\n[OPERATION: {op}]')

    # Ensure two sets are ready.
    if len(user_sets) < 2:
        print(f'Unable to perform {op} with less than two sets.')
        return
    
    # Prompt for two sets.
    set1 = user_sets[prompt_element('Enter the first set:', 'Set does not exist.', user_sets, True)]
    set2 = user_sets[prompt_element('Enter the second set:', 'Set does not exist.', user_sets, True)]
    res = set()

    # Operate.
    if op == 'UNION':
        res = set1.union(set2)
    elif op == 'INTERSECTION':
        res = set1.intersection(set2)
    elif op == 'SET DIFFERENCE':
        res = set1.difference(set2)

    # Display new set and save if needed.
    print_set('Result', res)
    save = utility.prompt_user_character('Would you like to save this set (Y/N)? ', ('Y', 'N'), False)

    if save == 'Y':
        create_set(user_sets, 'this set', res)
    else:
        print('\nResult discarded.')

def operate_set():
    '''Allows the user to perform set operations between existing sets and construct new sets from them.'''
    options = {
        ('U', 'Union'): (operate_given, ('UNION',)),
        ('I', 'Intersection'): (operate_given, ('INTERSECTION',)),
        ('S', 'Set Difference'): (operate_given, ('SET DIFFERENCE',)),
    }

    utility.handle_options('\n[SET OPERATIONS]', options, True, display_sets=(display_sets, tuple()))

def view_sets():
    '''Allows the user to view, build, edit, and delete sets. Additionally, new sets may be created through set operations.'''
    # Display options.
    options = {
        ('B', 'Build a New Set'): (build_new_set, tuple()),
        ('M', 'Modify a Set'): (edit_set, ('set', user_sets, print_set, display_sets, add_element_set, remove_element_set)),
        ('D', 'Delete a Set'): (delete_set, (user_sets, display_sets, 'set')),
        ('O', 'Operate on a Set'): (operate_set, tuple())
    }

    utility.handle_options('\n[VIEW SETS]', options, True, display_sets=(display_sets, tuple()))

############################################################################################

def prompt_pair(message, relation, should_exist):
    '''Prompts user for a pair of elements who must be from certain sets but whose pair
    may or may not exist in the relation.
    Args:
        message: A message that is output when the condition is not satisfied.
        relation: The relation to check.
        should_exist: Whether the condition should be satisfied when the element exists.
    Returns:
        tuple: The pair of elements.'''
    while True:
        # Display available sets.
        input_set_info = relation.get_io('INPUT')
        output_set_info = relation.get_io('OUTPUT')
        print_set(f'\nInput Set ({input_set_info[0]})', input_set_info[1])
        print_set(f'Output Set ({output_set_info[0]})', output_set_info[1])
        print()

        input_set = relation.get_io('INPUT')[1]
        output_set = relation.get_io('OUTPUT')[1]

        # Get elements from the relation's sets.
        input_element = prompt_element('Enter an element from the input set', 'This element does not exist.', input_set, True)
        output_element = prompt_element('Enter an element from the output set', 'This element does not exist.', output_set, True)
        pair = (input_element, output_element)

        # Determine whether the pair satisfies the condition.
        if not check_element(relation.get_roster(), pair, should_exist):
            print(f'\n{message}')
        else:
            return (input_element, output_element)

def get_pair_string(pair):
    '''Gets the ordered pair as a string.
    Args:
        pair: The tuple to be converted.
    Returns:
        str: The ordered pair.'''
    return f'({pair[0]}, {pair[1]})'

def print_relation(name, relation):
    '''Prints a relation's info.
    Args:
        name: The name of the relation.
        relation: The relation to print.'''
    input_name = relation.get_io('INPUT')[0]
    output_name = relation.get_io('OUTPUT')[0]
    print_set(f'{name} ({input_name}R{output_name})', relation.get_visual_roster())
    
def display_relations():
    '''Prints the user's relations.'''
    print(f'{'User Relations'}: {'None' if not user_rels else ''}')

    for name, relation in user_rels.items():
        print_relation(name, relation)

def add_element_relation(relation):
    '''Adds an element to a relation.
    Args:
        relation: The relation to update.'''
    # Check if more space exists.
    roster = relation.get_roster()

    if len(roster) >= len(relation.get_io('INPUT')[1]) * len(relation.get_io('OUTPUT')[1]):
        print('\nUnable to add more elements.')
        return

    # Prompt pair and add.
    user_element = prompt_pair('Element already exists.', relation, False)
    roster.add(user_element)
    print(f'{user_element} added.')

def remove_element_relation(relation):
    '''Removes an element from a set.
    Args:
        relation: The relation to update.'''
    roster = relation.get_roster()

    # Make sure there are still elements in the relation.
    if len(roster) == 0:
        print('No more elements to remove.')
        return
    
    user_element = prompt_pair('Element does not exist.', relation, True)
    roster.remove(user_element)

class Relation:
    def __init__(self):
        self.input_set = {}
        self.output_set = {}
        self.roster = set()

    def det_io(self, type):
        '''Returns the set of the relation to use.
        Args:
            type: The string of the type of set to use.
        Returns:
            set: The set to use.'''
        if type == 'INPUT':
            return self.input_set
        else:
            return self.output_set

    def set_io(self, type, name, user_set):
        '''Establishes a set that is part of a relation.
        Args:
            type: The type of set ('INPUT' or 'OUTPUT').
            name: The name of the set.
            user_set: The set to add.'''
        self.det_io(type)[name] = user_set

    def get_io(self, type):
        '''Gets an input or output set.
        Returns:
            tuple: The input or output set's name and set.'''
        used_set = self.det_io(type)
        name = list(used_set.keys())[0]
        return (name, used_set[name])

    def get_roster(self):
        '''Returns the roster form of the set.
        Returns:
            set: The relation as a set of ordered pairs.'''
        return self.roster
    
    def get_visual_roster(self):
        '''Returns the roster with its elements as strings.
        Returns:
            str: The roster with tuple elements converted to strings.'''
        visual_roster = set()

        for el in self.roster:
            visual_roster.add(get_pair_string(el))

        return visual_roster

def build_new_relation():
    '''Allows the user to build a new relation from two sets.'''
    new_relation = Relation()

    # Display sets and prompt for input and output sets.
    print('[BUILD RELATION]')
    display_sets()

    for i, type in enumerate(('INPUT', 'OUTPUT')):
        while True:
            decision = utility.prompt_user_character(f'Choose set #{i + 1} (C), or create one from scratch (S)? ', ('C', 'S'), False)
            user_name = ''
            user_set = set()
            print()

            if decision == 'C':
                if len(user_sets) > 0:
                    user_name = prompt_element('Enter your set', 'Set does not exist.', user_sets, True)
                    user_set = user_sets[user_name]
                else:
                    print('Insufficient sets.')
                    continue
            else:
                user_name, user_set = build_new_set()
        
            new_relation.set_io(type, user_name, user_set)
            break

    # Prompt user for ordered pairs.
    while True:
        # Prompt for elements from input set, then output set.
        add_element_relation(new_relation)
        print_set('Current Relation', new_relation.get_visual_roster())

        # Verify continuation.
        user_cont = utility.prompt_user_character('Continue (Y/N)? ', ('Y', 'N'), False)
        if user_cont == 'N':
            break

    # Prompt user for relation name.
    print()
    create_set(user_rels, 'this relation', new_relation)

def check_reflexive(relation):
    '''Checks if the relation is reflexive.
    Args:
        relation: The relation.
    Returns:
        boolean: Whether or not the relation is reflexive.'''
    roster = relation.get_roster()
    input_set = relation.get_io('INPUT')[1]

    for a in input_set:
        for (x, y) in roster:
            if a == y:
                break
        else:
            return False # No self-relation exists for the current domain element
    
    return True
    
def check_symmetric(relation):
    '''Checks if the relation is symmetric.
    Args:
        relation: The relation to check.
    Returns:
        boolean: Whether or not the relation is symmetric.'''
    roster = relation.get_roster()

    for (a, b) in roster:
        for (x, y) in roster:
            if a == y and b == x:
                break
        else:
            return False # No reversed pair exists for the current pair
    
    return True
    
def check_transitive(relation):
    '''Checks if the relation is transitive.
    Args:
        relation: The relation.
    Returns:
        boolean: Whether or not the relation is transitive.'''
    roster = relation.get_roster()

    for (a, b) in roster:
        for (c, d) in roster:
            if b == c:
                for (x, y) in roster:
                    if x == a and y == d:
                        break
                else:
                    return False # No chain exists between the two pairs
    
    return True

def is_equivalence_relation():
    '''Displays whether or not the relation is an equivalence relation and any other relevant properties.'''
    print('\n[PROPERTY ANALYSIS]')

    # Check if relations exist.
    if not user_rels:
        print(f'No relations to analyze.')
        return
    
    # Prompt user for a relation.
    display_relations()
    print()
    name = prompt_element('Enter the name of a relation', 'Relation does not exist.', user_rels, True)
    relation = user_rels[name]

    # Check for properties.
    reflexive = check_reflexive(relation)
    symmetric = check_symmetric(relation)
    transitive = check_transitive(relation)
    res = f'\n{name} is'

    # Evaluate results.
    if reflexive: res += '\n- Reflexive'
    if symmetric: res += '\n- Symmetric'
    if transitive: res += '\n- Transitive'

    if symmetric and reflexive and transitive:
        res += '\n∴ It is an equivalence relation.'
    else:
        res += '\n∴ It is not an equivalence relation.'

    print(res)

def view_relations():
    '''Allows the user to view, build, edit, and delete relations.'''
    # Display options.
    options = {
        ('B', 'Build a New Relation'): (build_new_relation, tuple()),
        ('M', 'Modify a Relation'): (edit_set, ('relation', user_rels, print_relation, display_relations, add_element_relation, remove_element_relation)),
        ('D', 'Delete a Relation'): (delete_set, (user_rels, display_relations, 'relation')),
        ('E', 'Equivalence Relation Check'): (is_equivalence_relation, tuple()),
    }

    utility.handle_options('\n[VIEW RELATIONSHIPS]', options, True, display_relations=(display_relations, tuple()))
# Name: Clarence Mariano
# Date: 4/16/2026
# Purpose: This program models the discrete math concepts of:
#          - Logic and truth tables
#          - Sets and relations
#          - Trees
#          - Algorithms
# Usage: Each discrete math concept can be accessed as options on a menu.

import sys
import logic_and_truth
import sets_and_relations
import utility

def display_logic_and_truth_guide():
    '''Displays the logic and truth guide.'''
    guide = 'This option allows you to create propositional statements and see how their variables interact to result in a truth value.\n\
These results can be condensed into a truth table, which you can view with option (C).\n\n\
Additionally, you may also write two statements and verify if third statement, or deduction rule, is valid through (T).\n\
These deduction rules must only be composed of variables found in the preceding statements.\n\n\
Lastly, you may enter statements to observe how they break down into their more atomic forms.\n\n\
Expression Info:\n\
\t- The available operators are as follows: xor, and, or, not, implies, iff\n\
\t- Variables and operators must be separated by spaces\n\
\t- Parentheses cannot be used as a part of variables'

    print('\n[LOGIC AND TRUTH TABLES GUIDE]')
    print(guide)
    utility.prompt_user_character('Enter anything to go back: ')
    return

def handle_logic_and_truth():
    '''Handles the logic and truth tables option.'''

    options = {
        ('C', 'Create a Truth Table'): (logic_and_truth.create_truth_table, tuple()),
        ('T', 'Test a Deduction Rule'): (logic_and_truth.create_deduction, tuple()),
        ('S', 'Simplify an Expression'): (logic_and_truth.break_statement, tuple()),
        ('G', 'User Guide'): (display_logic_and_truth_guide, tuple())
    }

    utility.handle_options('\nLOGIC AND TRUTH TABLES', options, True)

def display_sets_and_relations():
    '''Displays the sets and relations menu.'''
    print('\n[SETS AND RELATIONS]')
    print('\t(S) View Sets')
    print('\t(R) View Relations')
    print('\t(G) User Guide')

def display_sets_and_relations_guide():
    '''Displays the sets and relations guide.'''
    guide = ''

    print('\n[SETS AND RELATIONS GUIDE]')
    print(guide)
    utility.prompt_user_character('Enter anything to go back: ')
    return

def handle_sets_and_relations():
    '''Handles the sets and relations option.'''
    options = {
        ('S', 'View Sets'): (sets_and_relations.view_sets, tuple()),
        ('R', 'View Relations'): (sets_and_relations.view_relations, tuple()),
        ('G', 'User Guide'): (display_sets_and_relations_guide, tuple())
    }

    utility.handle_options('\n[SETS AND RELATIONS]', options, True)

def main():
    options = {
        ('L', 'Logic and Truth Tables'): (handle_logic_and_truth, tuple()),
        ('S', 'Sets and Relations'): (handle_sets_and_relations, tuple()),
        ('T', 'Trees'): None,
        ('A', 'Algorithms'): None,
        ('Q', 'Quit'): (lambda: (print('\nThank you for using the Discrete Structures Toolkit.'), sys.exit()), tuple())
    }

    utility.handle_options('\n[DISCRETE STRUCTURES TOOLKIT]', options, False)

main()
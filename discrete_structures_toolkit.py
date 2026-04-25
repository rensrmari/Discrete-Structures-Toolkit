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
import trees
import euclidean_algorithm
import utility

def display_logic_and_truth_guide():
    '''Displays the logic and truth guide.'''
    guide = 'This option allows you to create propositional statements and see how their variables interact to result in a truth value.\n\
These results can be condensed into a truth table, which you can view with option (C).\n\n\
Additionally, you may also write two statements and verify if third statement, or deduction rule, is valid through (T).\n\
These deduction rules must only be composed of variables found in the preceding statements.\n\n\
Lastly, you may enter statements to observe how they break down into their more atomic forms (S).\n\n\
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

def display_sets_and_relations_guide():
    '''Displays the sets and relations guide.'''
    guide = 'This option allows you to construct sets and relations. Sets can be created through (S) and enable the creation of new\n\
sets through the use of operations (O), including union (U), intersection (I), and set difference (S).\n\
Sets are created one element at a time and must have unique values.\n\n\
Relations are constructed similarly, one pair at a time, one element at a time. However, the input and output sets\n\
must be specified beforehand and are limited by the Cartesian product.\n\n\
After creating a relation, they can then be analyzed for properties such as reflexivity, symmetry, and transitivity (E).'

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

def display_trees_guide():
    '''Displays the guide for the trees option.'''
    guide = 'This option allows you to build trees, edit them, and analyze them.\n\
Analyzing trees is enabled through the ability to visualize them, search for a value, and traverse them element-by-element.\n\n\
The method used to traverse these trees is depth-first, with containers tracking visited elements due to these trees having\n\
variable numbers of children.\n\n\
NOTE: Exiting the tree editor may involve going back multiple times, due to being deep in the branches of the tree.\n\
Once you reach the root node, you will be able to return to the previous menu; your location in the tree can be located\n\
near the header.'

    print('\n[TREES GUIDE]')
    print(guide)
    utility.prompt_user_character('Enter anything to go back: ')
    return

def handle_trees():
    '''Handles the trees option.'''
    options = {
        ('C', 'Create Root'): (trees.create_root, tuple()),
        ('V', 'View Trees'): (trees.view_trees, tuple()),
        ('G', 'User Guide'): (display_trees_guide, tuple()),
    }

    utility.handle_options('\n[TREES]', options, True)

def display_algorithms_guide():
    '''Displays the guide for the algorithms option.'''
    guide = 'This option allows you to observe the Euclidean algorithm, which is an iterative and relatively efficient approach to\n\
calculating the greatest common factor between two integers.\n\n\
You will be prompted to enter two integers and can view the algorithm\'s step-by-step process shortly after.'

    print('\n[ALGORITHMS GUIDE]')
    print(guide)
    utility.prompt_user_character('Enter anything to go back: ')
    return

def handle_algorithms():
    '''Handles the algorithms option.'''
    options = {
        ('E', 'Observe the Euclidean Algorithm'): (euclidean_algorithm.euclidean_algorithm, tuple()),
        ('G', 'User Guide'): (display_algorithms_guide, tuple())
    }

    utility.handle_options('\n[EUCLIDEAN ALGORITHM]', options, True)

def main():
    options = {
        ('L', 'Logic and Truth Tables'): (handle_logic_and_truth, tuple()),
        ('S', 'Sets and Relations'): (handle_sets_and_relations, tuple()),
        ('T', 'Trees'): (handle_trees, tuple()),
        ('A', 'Algorithms'): (handle_algorithms, tuple()),
        ('Q', 'Quit'): (lambda: (print('\nThank you for using the Discrete Structures Toolkit.'), sys.exit()), tuple())
    }

    utility.handle_options('\n[DISCRETE STRUCTURES TOOLKIT]', options, False)

main()
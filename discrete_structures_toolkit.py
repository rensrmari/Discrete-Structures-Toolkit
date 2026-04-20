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
import utility

def display_main_menu():
    '''Prints the main menu.'''
    print('\n[DISCRETE STRUCTURES TOOLKIT]')
    print('\t(L) Logic and Truth Tables')
    print('\t(S) Sets and Relations')
    print('\t(T) Trees')
    print('\t(A) Algorithms')
    print('\t(Q) Quit')

def display_logic_and_truth():
    '''Displays the logic and truth table menu.'''
    print('\n[LOGIC AND TRUTH TABLES]')
    print('\t(C) Create a Truth Table')
    print('\t(T) Test a Deduction Rule')
    print('\t(S) Simplify an Expression')
    print('\t(G) User Guide')

def handle_logic_and_truth():
    while True:
        # Display options.
        display_logic_and_truth()
        ch = utility.prompt_user_character('Enter a character, or anything else to go back: ')

        if ch == 'C':
            print('\n[TRUTH TABLE]')
            logic_and_truth.create_truth_table()
        elif ch == 'T':
            print('\n[DEDUCTION RULE]')
            logic_and_truth.create_deduction() 
        elif ch == 'S':
            print('\n[STATEMENT SIMPLIFICATION]')
            logic_and_truth.break_statement()
        elif ch == 'G':
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
        else:
            return

def main():
    while True:
        # Display main menu options.
        display_main_menu()
        ch = utility.prompt_user_character('Enter a character: ')

        if ch == 'L':
            handle_logic_and_truth()
        elif ch == 'S':
            pass
        elif ch == 'T':
            pass
        elif ch == 'A':
            pass
        elif ch == 'Q':
            print('\n Thank you for using the Discrete Structures Toolkit.')
            sys.exit()
        else:
            print('Invalid character.')

main()
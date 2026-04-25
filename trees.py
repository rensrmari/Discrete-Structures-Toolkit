import utility

user_trees = {}

def display_trees():
    '''Displays the user's trees.'''
    print(f'{'User Trees'}: {'None' if not user_trees else ''}')

    for name, node in user_trees.items():
        print(f'{name}: Root - {node.value}')

def display_node_info(node):
    # Display node and its children.
    children = node.children
    print(f'Current Node: {node.value}')
    print(f'Children: ', end=f'{'None' if not children else ''}')

    for child in children:
        print(child.value, end=' ')

    print()

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def aux_dfs(root, visited, children, value):
    try:
        remaining = get_left(visited, children)
        next_node = remaining.pop()
        visited.add(next_node)
        success = dfs(root, visited, next_node, value)

        if success:
            return True
    except IndexError:
        dfs(root, visited, root, value)

def dfs(root, visited, node, value):
    # Check if all children have been visited, without locating the value.
    if len(get_left(visited, root.children)) <= 0:
        return False
    
    # Print current value.
    print(node.value, end=' ')

    # Check for null node.
    if not node:
        return
    
    # Check for value.
    if node.value == value:
        return True

    # Get children to search.
    return aux_dfs(root, visited, node.children, value)

def search_tree(root):
    # Display tree.
    print('Tree:')
    print_tree(root)

    # Get value.
    value = input('Enter a value to look for: ')
    print('Searched Values: ', end='')
    found = dfs(root, set(), root, value)
    print()

    if found:
        print('\nValue found!')
    else:
        print('\nCould not find value.')

def print_tree(node, tab):
    print(f'{tab}{node.value}')

    for child in node.children:
        print_tree(child, tab + '\t')

def get_left(visited, children):
    children = children.copy()
    for el in visited:
        if el in children:
            children.remove(el)

    return children

def continue_tree(root, visited, children):
    try:
        remaining = get_left(visited, children)
        next_node = remaining.pop()
        visited.add(next_node)
        edit_tree(root, visited, next_node)
    except IndexError:
        print('\nFinished branch.')
        edit_tree(root, visited, root)

def add_child(parent):
    user_val = input('Enter a value for this child: ')
    new_node = Node(user_val)
    parent.children.append(new_node)

def edit_tree(root, visited, node):
    '''Allows the user to modify the tree, branch by branch.
    Args:
        node: The current node.'''
    # Check for visited nodes.
    if len(get_left(visited, root.children)) <= 0:
        visited = set()

    # Check for null node.
    if not node:
        print('\nFinished branch.')
        return
    
    # Present user options.
    options = {
        ('P', 'Print Tree'): (print_tree, (root,'')),
        ('C', 'Continue through the Tree'): (continue_tree, (root, visited, node.children)),
        ('A', 'Add Child Below'): (add_child, (node,))
    }

    utility.handle_options('\n[TREE EDITOR]', options, True, display_node_info=(display_node_info, (node,)))

def select_tree():
    print('\n[TREE SELECTION]')

    '''Allows user to select an existing tree, and then print, edit, and search it.'''
    # Check if trees exist.
    if not user_trees:
        print('No trees to select.')
        return

    # Prompt user for a tree.
    name = utility.prompt_element('Enter the name of your tree', 'Tree does not exist.', user_trees, True)
    node = user_trees[name]

    options = {
        ('E', 'Edit Tree'): (edit_tree, (node, set(), node)),
        ('S', 'Search Tree'): (search_tree, (node,))
    }

    utility.handle_options(f'\n[SELECTED TREE: {name}]', options, True)

def create_root():
    '''Allows the user to begin a new tree.'''
    # Prompt user for a value and create a node.
    user_val = input('Enter a value for the root: ')
    node = Node(user_val)

    # Get a name for the tree.
    name = utility.prompt_element('Enter a name for the tree', 'Name is already taken.', user_trees, False)
    user_trees[name] = node

def view_trees():
    '''Allows the user to see their trees and select or delete them.'''
    # Display options.
    options = {
        ('S', 'Select a Tree'): (select_tree, tuple()),
        ('D', 'Delete a Tree'): (utility.delete_set, (user_trees, display_trees, 'tree'))
    }

    utility.handle_options('\n[VIEW TREES]', options, True, display_trees=(display_trees, tuple()))
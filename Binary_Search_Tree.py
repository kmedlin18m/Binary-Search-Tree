import queue


# --------------------------------------
# Program Title: User Interface to BST
# Author: Kirsten Medlin
# Class: CSCI3320 Fall 2022
# Programming Assignment #2
# --------------------------------------


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# ----------------------------------------------------------
# FUNCTION printTree : Print tree
#    Recursive function to print the tree in descending order
# INPUT PARAMETERS :
#     root: the root of the tree or current subtree
# OUTPUT :
#     Keys of the tree nodes
# ----------------------------------------------------------
def printTree(root):
    # Base case
    if root is None:
        return
    printTree(root.right)
    print(root.data, end=' ')
    printTree(root.left)


# ---------------------------------------------------------
# FUNCTION insert : insert
#    Recursive function to insert a key into a BST
# INPUT PARAMETERS :
#    root: root node of current tree/subtree
#    key: integer that will be turned into a key in the BST
# OUTPUT :
#    Nothing
# ---------------------------------------------------------
def insert(root, key):
    # if the root is None, create a new node and return it
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# --------------------------------------------------
# FUNCTION numLeaves : Number of Leaves
#   Recursively prints number of leaves in a tree
# INPUT PARAMETERS :
#    root: root node of the current tree/subtree
# OUTPUT :
#    Returns the total number of leaves
# --------------------------------------------------
def numLeaves(root):
    # Base case
    if root is None:
        return 0
    if (root.left is None and root.right is None):
        return 1
    return numLeaves(root.left) + numLeaves(root.right)


# ----------------------------------------------------------
# FUNCTION numOneChildNodes : Number of nodes with one child
#   Recursively counts how many nodes have only one child.
# INPUT PARAMETERS :
#    root: root node of current tree/subtree
# OUTPUT:
#    returns count, which is the variable storing the
#    number of nodes with one child
# ----------------------------------------------------------
def numOneChildNodes(root):
    # Base case:
    if root is None:
        return 0
    count = 0
    if root.left is None and root.right is not None:
        count += 1
    elif root.left is not None and root.right is None:
        count += 1

    count += numOneChildNodes(root.left) + numOneChildNodes(root.right)
    return count


#--------------------------------------------------------------------
# FUNCTION numTwoChildren : Number of nodes with two children
#   Recursively counts nodes with two children
# INPUT PARAMETERS :
#    root: root node of current tree/subtree
# OUTPUT :
#    returns count, which is the variable that keeps track of how many
#    nodes have two children
#--------------------------------------------------------------------
def numTwoChildrenNodes(root):
    # Base case:
    if root is None:
        return 0
    count = 0
    if root.left is not None and root.right is not None:
        count += 1
    count += numTwoChildrenNodes(root.left) + numTwoChildrenNodes(root.right)
    return count


#----------------------------------------
# FUNCTION levelOrder : Level Order
#   Prints tree in level order traversal
# INPUT PARAMETERS :
#   root: Root of tree
# OUTPUT :
#   Prints node keys
#----------------------------------------
def levelOrder(root):
    # Base case
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while (not q.empty()):
        n = q.get()
        print(n.data, end=' ')
        if n.left is not None:
            q.put(n.left)
        if n.right is not None:
            q.put(n.right)
    return


#-------------------------------------------------------------------
# FUNCTION rangeOfTree : Range of Tree
#   Recursively prints keys of tree that are in the range k1 and k2
# INPUT PARAMETERS :
#   k1 : lower bound
#   k2 : upper bound
# OUTPUT :
#   Prints node key if its in range of k1 and k2
#-------------------------------------------------------------------
def rangeOfTree(k1, k2, root):
    # Base case
    if root is None:
        return
    if k1 < root.data:
        rangeOfTree(k1, k2, root.left)
    if k1 <= root.data and k2 >= root.data:
        print(root.data, end=' ')
    if k2 > root.data:
        rangeOfTree(k1, k2, root.right)


if __name__ == '__main__':

    user_input = 0
    keys = []
    keys_input = 0

    while user_input != "8":

        # Menu
        print("\n>>Enter choice [1-8] from menu below:")
        print("1) Construct a tree")
        print("2) Print in descending order")
        print("3) Print number of leaves in tree")
        print("4) Print number of nodes with only one child")
        print("5) Print the number of nodes that contain two children")
        print("6) Print the level order traversal of the tree")
        print("7) Print all elements in the tree between k1 and k2")
        print("8) Exit program")

        user_input = input("Option: ")
        print()

        # Option 1: Construct a tree
        if user_input == "1":
            keys_input = input("Enter initial elements: (please separate values by spaces): ")
            keys = keys_input.split()

            # convert list to integers
            keys = [int(x) for x in keys]

            # Insert user list into BST
            root = None
            for key in keys:
                root = insert(root, key)
            print("\nValues have been inserted!")

        # Option 2: Print in descending order
        if user_input == "2":
            print("Print in descending order: ", end='')
            printTree(root)
            print('')

        # Option 3: Print number of leaves
        if user_input == "3":
            print("Number of leaves: ", end='')
            print(numLeaves(root))

        # Option 4: Print nodes with one child
        if user_input == '4':
            print("Nodes with one child: ", end='')
            print(numOneChildNodes(root))

        # Option 5: Print nodes with two children
        if user_input == '5':
            print("Nodes with two children: ", end='')
            print(numTwoChildrenNodes(root))

        # Option 6: Print in level order
        if user_input == '6':
            print("Level order: ", end='')
            levelOrder(root)
            print()

        # Option 7: Print elements between k1 and k2
        if user_input == '7':
            k1 = int(input("Enter k1 (lower bound): "))
            k2 = int(input("Enter k2 (upper bound): "))
            rangeOfTree(k1, k2, root)
            print()

from binarytree import build 

class Node:
    
    #A class representing a node in binary tree
    def __init__(self,key):
        self.left = None
        self.val= key
        self.right = None
        
def print_inorder(root):
    #Recursively performs an inorder traversal of the binary tree
    if root:
        #Recursively traverse the left subtree
        print_inorder(root.left)
        
        #Print the data of the node
        print(root.val, end=' ')
        
        #Recursively traverse the right subtree
        print_inorder(root.right)
        
if __name__== "__main__":
    #Constructing the binary tree
    root= Node(1)
    root.left= Node(2)
    root.right= Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)
    
    #Using the binary tree module to visualize the tree structure
    #Convert the tree into a binarytree node structure
    tree_list= [1, 2, 3, 4, 5]
    visual_tree= build(tree_list)
    
    print("\nBinary Tree Visualization: ")
    print(visual_tree)
    
    #Printing inorder traversal
    print_inorder(root)
    print()
from binarytree import build 

class Node:
    
    #A class representing a node in a binary tree
    
    def __init__(self, key):
        self.val= key
        self.left= None
        self.right= None
        
def print_postorder(root):
    if root:
        #Recursively traverse the left subtree
        print_postorder(root.left)
        
        #Recursively travere the right subtree
        print_postorder(root.right)
        
        #Print the data of the node
        print(root.val, end=' ')
        
if __name__== "__main__":
    #Constructing the binary tree
    root= Node(1)
    root.left= Node(2)
    root.right= Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)
    
    #Using the binarytree module to visualize the tree structure
    #Convert the tree into a binary node structure
    
    tree_list= [1, 2, 3, 4, 5]
    visual_tree= build(tree_list)
    
    print("\nBinary Tree Conversion")
    print(visual_tree)
    
    #Printing the postorder traversal of the binary tree
    print("Post order Traversal of the binary tree is: ")
    print_postorder(root)
    print()
    
    
"""
@Question
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if(self.root == None):
            self.root = Node(data)
            return
        temp = self.root
        while(temp != None):
            if(temp.data > data):
                if(temp.left != None):
                    temp = temp.left
                else:
                    temp.left = Node(data)
                    return
            elif(temp.data < data):
                if(temp.right != None):
                    temp = temp.right
                else:
                    temp.right = Node(data)
                    return
            else:
                print("Data already present")
                return

    def preorder(self, node):
        if(node == None):
            return
        print node.data,
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if(node == None):
            return
        self.inorder(node.left)
        print node.data,
        self.inorder(node.right)
        
 
    def postorder(self, node):
        if(node== None):
            return
        self.inorder(node.left)
        self.inorder(node.right)
        print node.data,

    def min_path_sum(self, node):
        if(node.right == None and node.left == None):
            return node.data
            
        if(node.right != None):
            right_value = node.data + self.min_path_sum(node.right)
        if(node.left != None):
            left_value =  node.data + self.min_path_sum(node.left)

        if(node.right != None and node.left != None):
            if(right_value < left_value):
                return right_value
            else: return left_value
        elif(node.right != None): return right_value
        else: return left_value


tree = BinaryTree()
for i in [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]:
    tree.insert(i)
tree2 = BinaryTree()
for i in [10, 11, 5, 1, -1]:
    tree2.insert(i)

tree.preorder(tree.root)
print "\n"
tree.inorder(tree.root)
print "\n"
tree.postorder(tree.root)
print "\n"
print(tree2.min_path_sum(tree2.root))

"""
@Solution_comment
The solution works for any binary tree, through the insertion method 
above follows the formal insertion procedure of a binary tree.

"""
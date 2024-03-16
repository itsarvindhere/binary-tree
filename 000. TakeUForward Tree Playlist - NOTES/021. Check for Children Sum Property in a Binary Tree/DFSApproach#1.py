class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # DFS
    def dfs(self, root):
        
        # Base case
        if not root: return -1
       
        # Traverse left
        left = self.dfs(root.left)
       
        # Traverse right
        right = self.dfs(root.right)
       
        # If it is a leaf node, then it follows the property
        # So, return its value to be used in the previous recursive call
        if left == -1 and right == -1: return root.val
        
        # If the left subtree or right subtree does not follow the children sum property, return 0
        if left == 0 or right == 0: return 0
        
        # Check if current "root" node follows the Children Sum property
        
        # If the left child is Null, the root node's value must be equal to right node's value
        if left == -1 and root.val != right: return 0
        
        # If the right child is Null, the root node's value must be equal to left node's value
        elif right == -1 and root.val != left: return 0
        
        # If both the left and right child exist, the root node's value must be equal to the sum of left and right values
        elif left != -1 and right != -1 and root.val != left + right: return 0
        
        # The current subtree with "root" node follows the Children Sum Property
        return root.val
    
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        
        # If the tree does not follow Children Sum Property, the 'dfs' method will return 0
        return 0 if self.dfs(root) == 0 else 1


root = TreeNode(45)
root.left = TreeNode(35)
root.right = TreeNode(10)
root.left.left = TreeNode(30)
root.left.right = TreeNode(5)
root.right.left = TreeNode(8)
root.right.right = TreeNode(2)

print("Output -> ", Solution().isSumProperty(root))
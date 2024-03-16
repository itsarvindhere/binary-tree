class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        
        # BASE CASE
        if not root or (not root.left and not root.right): return 1
        
        # VALUES OF LEFT AND RIGHT CHILDREN
        left,right = 0,0
        
        if root.left: left = root.left.val
        if root.right: right = root.right.val
        
        # CHECK IF THE ROOT NODE FOLLOWS THE CHILDREN SUM PROPERTY
        if root.val != left + right: return 0
        
        # IF IT DOES, CHECK IF THE LEFT AND RIGHT SUBTREES FOLLOW THE PROPERTY
        return self.isSumProperty(root.left) and self.isSumProperty(root.right)


root = TreeNode(45)
root.left = TreeNode(35)
root.right = TreeNode(10)
root.left.left = TreeNode(30)
root.left.right = TreeNode(5)
root.right.left = TreeNode(8)
root.right.right = TreeNode(2)

print("Output -> ", Solution().isSumProperty(root))
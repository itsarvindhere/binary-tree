class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive Function
    def isMirror(self, left, right):
        
        # If one or both are Null, return True if both are Null
        # Otherwise return False
        if not left or not right: return left == right
    
        # The left and right nodes need to have same values
        # And their mirror nodes also need to be the same
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    
    def isSymmetric(self, root):
        
        # Call the recursive function
        return self.isMirror(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)

print("Is the Tree Symmetric? ", Solution().isSymmetric(root))
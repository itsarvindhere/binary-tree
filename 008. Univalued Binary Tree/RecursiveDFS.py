class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive function to check for a univalued tree
    def check(self, root, val):
        
        # Base Case
        if not root: return True
        
        # A tree is univalued if the root has same value that all nodes need to have
        # And the left and right subtrees are univalued
        return root.val == val and self.check(root.left, val) and self.check(root.right, val)
        
    
    def isUnivalTree(self, root):
        
        # Call the recursive function to check if the tree is univalued
        return self.check(root, root.val)


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)

print("Output -> ", Solution().isUnivalTree(root))
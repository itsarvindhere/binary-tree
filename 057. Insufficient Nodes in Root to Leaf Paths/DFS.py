# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root, limit):
        
        # Base Case
        if not root: return None
        
        # If this is a leaf node
        if not root.left and not root.right: 
            
            # If the value is >= limit
            # It means, the root to this leaf path is a valid path
            # Hence, return this node back for the previous recursive calls
            if root.val >= limit: return root
            
            # Otherwise, this path is not valid so return "None"
            else: return None
		
		# If current "root" node is not a leaf node
		
        # What does the left recursive call gives us
        root.left = self.sufficientSubset(root.left, limit - root.val)
        
        # What does the right recursive call gives us
        root.right = self.sufficientSubset(root.right, limit - root.val)
        
        # If left and right are "None"
        # It means, all the root to leaf paths intersecting the current "root" node are invalid
        # So, return "None" in this case
        if not root.left and not root.right: return None
        
        # Otherwise, return the root node
        return root

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(1)
root.right.left = TreeNode(17)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(3)

limit = 22

print("Output -> ", Solution().sufficientSubset(root, limit))
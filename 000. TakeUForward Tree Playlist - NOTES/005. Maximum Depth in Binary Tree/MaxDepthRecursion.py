class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def maxDepth(self, root) -> int:
        
        # Base case
        if not root: return 0
        
        # Height of left subtree
        lHeight = self.maxDepth(root.left)
        
        # Height of right subtree
        rHeight = self.maxDepth(root.right)
        
        # Return the max out of the two
        return max(lHeight,rHeight) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Maximum depth of the tree is -> ", Solution().maxDepth(root))


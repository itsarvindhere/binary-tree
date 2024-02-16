class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive function to get the height of a Binary Tree
    def getHeight(self, root, diameter):
        
        # Base case
        if not root: return 0
        
        # Get the left height
        lHeight = self.getHeight(root.left, diameter)
        
        # Get the right height
        rHeight = self.getHeight(root.right, diameter)
        
        # Update the diameter
        diameter[0] = max(diameter[0], lHeight + rHeight)
        
        # Return the maximum of the two, plus 1
        return max(lHeight, rHeight) + 1

    
    def diameterOfBinaryTree(self, root) -> int:
        
        # Diameter to return
        diameter = [0]
        
        # Call the recursive function
        self.getHeight(root, diameter)
        
        # Return the diameter of the Binary Tree
        return diameter[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter ->", Solution().diameterOfBinaryTree(root))
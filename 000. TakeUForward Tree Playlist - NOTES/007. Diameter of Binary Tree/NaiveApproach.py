class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive function to get the height of a Binary Tree
    def getHeight(self, root):
        
        # Base case
        if not root: return 0
        
        # Get the left height
        lHeight = self.getHeight(root.left)
        
        # Get the right height
        rHeight = self.getHeight(root.right)
        
        # Return the maximum of the two, plus 1
        return max(lHeight, rHeight) + 1
    
    # Recursive function to get the length of longestpath that crosses through a "node" 
    def getDiameter(self, root, diameter):
        
        # Base case
        if not root: return 0
        
        # For current root, get the longest path that goes through it
        # And update the diamter accordingly
        diameter[0] = max(diameter[0], self.getHeight(root.left) + self.getHeight(root.right))
        
        # Make a recursive call for left and right
        self.getDiameter(root.left, diameter)
        self.getDiameter(root.right, diameter)

    
    def diameterOfBinaryTree(self, root) -> int:
        
        # Diameter to return
        diameter = [0]
        
        # Call the recursive function
        self.getDiameter(root, diameter)
        
        # Return the diameter of the Binary Tree
        return diameter[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter ->", Solution().diameterOfBinaryTree(root))
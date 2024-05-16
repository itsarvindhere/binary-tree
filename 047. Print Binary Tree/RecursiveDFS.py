# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to get the height of the tree
    def getHeight(self, root):
        
        # Base Case
        if not root: return 0
        
        # Left Height
        leftHeight = self.getHeight(root.left)
        
        # Right Height
        rightHeight = self.getHeight(root.right)
        
        # Return the height
        return max(leftHeight, rightHeight) + 1
    
    # Traverse the tree and put the values in the output list
    def dfs(self, root, r, c, height, output):
        
        # Base Case
        if not root: return
        
        # Put the value at the correct place in the output list
        output[r][c] = str(root.val)
        
        # Traverse left
        self.dfs(root.left, r + 1, (c - (2**(height - r - 1))), height, output)
        
        # Traverse right
        self.dfs(root.right, r + 1, (c + (2**(height - r - 1))), height, output)
    
    def printTree(self, root):
        
        height = self.getHeight(root) - 1
        
        # Number of rows
        m = height + 1
        
        # Number of columns
        n = (2**(height + 1)) - 1
        
        # Create an output 2D matrix with m rows and n columns, initially with ""
        output = [[""] * n for i in range(m)]
        
        # Traverse the tree in DFS and put the values at correct places
        self.dfs(root, 0, n//2, height, output)
        
        # Return the output list
        return output

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print("Output ->", Solution().printTree(root))
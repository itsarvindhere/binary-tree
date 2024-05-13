# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive DFS function
    def dfs(self, root, level, maxValues):
        
        # Base Case
        if not root: return
        
        # Update the maximum for current level
        if level in maxValues: maxValues[level] = max(maxValues[level], root.val)
        else: maxValues[level] = root.val
        
        # Traverse left
        self.dfs(root.left, level + 1, maxValues)
        
        # Traverse right
        self.dfs(root.right, level + 1, maxValues)
    
    def largestValues(self, root):
        
        # A dictionary to keep track of the level and the maximum value at that level
        maxValues = {}
        
        # Call the recursive dfs function
        self.dfs(root, 0, maxValues)
        
        # Output list to return
        output = []
        
        # Iterate over the dictionary and put the maximum values for each level in the output list
        for level in maxValues: output.append(maxValues[level])
        
        # Finally, return the output list
        return output

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

print("Output -> ", Solution().largestValues(root))
from collections import deque
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # DFS Traversal
    def dfs(self, root, level, levelSum):
        
        # Base Case
        if not root: return
        
        # Update the sum for the current level
        levelSum[level] = levelSum.get(level,0) + root.val
        
        # Traverse left
        self.dfs(root.left, level + 1, levelSum)
        
        # Traverse right
        self.dfs(root.right, level + 1, levelSum)
    
    def maxLevelSum(self, root):
        
        # To keep track of the maximum level sum
        maxSum = -inf
        
        # To keep track of the level with the maximum sum
        maxSumLevel = -1
        
        # To keep track of the sum of each level
        levelSum = {}
        
        # Call the dfs function to traverse the tree and get the level sum
        self.dfs(root, 1, levelSum)
        
        # Now, just traverse the dictionary and get the level with the maximum sum
        for level in levelSum:
            if levelSum[level] > maxSum:
                maxSum = levelSum[level]
                maxSumLevel = level
                
        # Finally, return the level with the maximum sum
        return maxSumLevel

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

print("Output -> ", Solution().maxLevelSum(root))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to find the maximum difference
    def dfs(self, root, minAncestorValue, maxAncestorValue, maxDiff):
        
        # Base Case
        if not root: return
        
        # Update the max Diff accordingly
        maxDiff[0] = max(maxDiff[0], abs(root.val - minAncestorValue), abs(root.val - maxAncestorValue))
        
        # Traverse left
        self.dfs(root.left, min(minAncestorValue, root.val), max(maxAncestorValue, root.val), maxDiff)
        
        # Traverse right
        self.dfs(root.right, min(minAncestorValue, root.val), max(maxAncestorValue, root.val), maxDiff)
    
    
    def maxAncestorDiff(self, root) -> int:
        
        # Maximum difference to return
        maxDiff = [0]
        
        # A Helper function to find the maximum ancestor difference
        # The function will be passed the node (initially root)
        # Along with the minimum ancestor value so far (initially just the root value)
        # And also the maximum ancestor value so far (initially just the root value)
        # Because for any node, the maximum difference between it and its ancestor
        # Will be either between its value and the minimum ancestor value, or
        # its value and the maximum ancestor value
        self.dfs(root, root.val, root.val, maxDiff)
        
        # Return the maximum difference
        return maxDiff[0]

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)
root.left.right.left = TreeNode(4)
root.right.right.right = TreeNode(7)

print("Output -> ", Solution().maxAncestorDiff(root))
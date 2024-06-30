# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Recursive function to get the longest path
    def dfs(self, root, val, longestPath):
        
        # Base Case
        if not root: return 0
        
        # Get the longest univalue path on left where the nodes have same value as root
        leftPath = self.dfs(root.left, root.val, longestPath)
        
        # Get the longest univalue path on the right where the nodes have same value as root
        rightPath = self.dfs(root.right, root.val, longestPath)
        
        # Update the longest path
        longestPath[0] = max(longestPath[0], leftPath + rightPath)
        
        # Return the appropriate value back for previous recursive calls
        return 1 + max(leftPath, rightPath) if root.val == val else 0
    
    def longestUnivaluePath(self, root) -> int:
        
        # The length of the longest path to return
        longestPath = [0]
        
        # If there are no nodes
        if not root: return 0
        
        # Call the recursive function to get the longest path
        self.dfs(root, root.val, longestPath)
        
        # Return the longest path
        return longestPath[0]

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

print("Output -> ", Solution().longestUnivaluePath(root))
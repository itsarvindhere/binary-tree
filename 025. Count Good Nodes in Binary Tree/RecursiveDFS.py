
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # DFS Traversal
    def dfs(self, root, maxSoFar, count):
        
        # Base Case
        if not root: return
        
        # If maxSoFar is <= root node's value, then it means root node is a good node
        if maxSoFar <= root.val:
            count[0] += 1
            maxSoFar = root.val
        
        # Traverse left
        self.dfs(root.left, maxSoFar, count)
        
        # Traverse right
        self.dfs(root.right, maxSoFar, count)
    
    
    def goodNodes(self, root) -> int:
        
        # Count of good nodes
        count = [0]
        
        # Helper function for traversal
        self.dfs(root, root.val, count)
        
        # Return the count
        return count[0]

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print("Output -> ", Solution().goodNodes(root))
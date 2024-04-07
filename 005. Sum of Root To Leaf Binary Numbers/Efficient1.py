# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Helper Function for Recursive DFS
    def dfs(self, root, totalSum):
        
        # Base case
        if not root: return 0
        
        # Update the total Sum
        totalSum = (2* totalSum) + root.val
        
        # If this is a leaf node
        if not root.left and not root.right: return totalSum
        
        # Make recursive calls for left and right subtrees
        return self.dfs(root.left, totalSum) + self.dfs(root.right, totalSum)
    
    def sumRootToLeaf(self, root) -> int:
        
        # Return the total sum
        return self.dfs(root, 0)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print("Total Sum -> ", Solution().sumRootToLeaf(root))
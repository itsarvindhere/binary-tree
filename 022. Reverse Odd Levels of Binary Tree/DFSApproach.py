# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Helper function for DFS
    def dfs(self, left, right, level):
        
        # Base Case
        if not left or not right: return
        
        # If this is an odd level
        # Swap the node values
        if level % 2 != 0: left.val, right.val = right.val, left.val
            
        # Traverse left
        self.dfs(left.left, right.right, level + 1)
        
        # Traverse right
        self.dfs(left.right, right.left, level + 1)
    
    
    def reverseOddLevels(self, root):
        
        # If there is only one node
        if not root.left: return root
        
        # Helper function for DFS
        # It takes three arguments
        # The two nodes passed are always the ones whose values need to be swapped
        # The third value is the level
        self.dfs(root.left, root.right, 1)
        
        # Finally, we can return the root node
        return root

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)

print("Output -> ", Solution().reverseOddLevels(root))
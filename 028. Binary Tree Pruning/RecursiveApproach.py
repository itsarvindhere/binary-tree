# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Recursive function to traverse the tree
    def dfs(self, root):
        
        # Base Case
        if not root: return False
        
        # Check if there is at least one "1" on the left side
        isOneOnLeft = self.dfs(root.left)
        
        # Check if there is at least one "1" on the right side
        isOneOnRight = self.dfs(root.right)

        # If there is not even a single "1" on the left side, the whole left subtree will have to be pruned
        if not isOneOnLeft: root.left = None
            
        # If there is not even a single "1" on the right side, the whole right subtree will have to be pruned
        if not isOneOnRight: root.right = None     
        
        # If the current subtree has to be pruned as well, return False
        if not isOneOnLeft and not isOneOnRight and root.val == 0: return False
        
        # Return True
        return True
        
    
    def pruneTree(self, root):
        
        # Call the recursive function
        result = self.dfs(root)
        
        # If the result of the dfs function is False, it means the entire tree needs to be pruned
        # So, it means after pruning, nothing will be left
        if not result: return None
        
        # Return the root after pruning the tree
        return root
        

root = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print("Output -> ", Solution().pruneTree(root))
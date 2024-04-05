# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root):
        
        # Base Case
        if not root: return
        
        # If it is a leaf node
        if not root.left and not root.right: return True if root.val == 1 else False
        
        # Evaluate the left subtree
        leftTreeResult = self.evaluateTree(root.left)
        
        # Evaluate the right subtree
        rightTreeResult = self.evaluateTree(root.right)
        
        # Return the final value
        return (leftTreeResult and rightTreeResult) if root.val == 3 else (leftTreeResult or rightTreeResult)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print("Output -> ", Solution().evaluateTree(root))
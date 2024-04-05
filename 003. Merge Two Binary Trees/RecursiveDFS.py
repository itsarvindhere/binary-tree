# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        
        # Base Case
        # If either both "root1" and "root2" are Null
        # Or, one of them is Null
        if not root1 or not root2: return root1 if not root2 else root2
        
        # Merge the node values
        root1.val += root2.val
        
        # Merge the left subtrees
        root1.left = self.mergeTrees(root1.left, root2.left)
        
        # Merge the right subtrees
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        # Return the final tree
        return root1

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

print("Output -> ", Solution().mergeTrees(root1,root2))
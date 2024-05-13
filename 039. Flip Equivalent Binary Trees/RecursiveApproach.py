# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def flipEquiv(self, root1, root2):
        
        # Base Case
        if not root1 or not root2: return root1 == root2
        
        # If root1 has same value as root2, then we will compare their children
        return root1.val == root2.val and (self.flipEquiv(root1.left, root2.left) or self.flipEquiv(root1.left, root2.right)) and (self.flipEquiv(root1.right, root2.right) or self.flipEquiv(root1.right, root2.left))


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)

root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.left.right = TreeNode(6)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
root2.right.right.left = TreeNode(8)
root2.right.right.right = TreeNode(7)
        
print("Output -> ", Solution().flipEquiv(root1,root2))
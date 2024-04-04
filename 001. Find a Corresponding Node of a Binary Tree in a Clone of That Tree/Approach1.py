class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # BFS
    def bfs(self, root, target):
        
        # BASE CASE
        if not root: return -1
        
        # If the current "root" node's value is same as target
        # We found the correct node
        if root.val == target.val: return root
        
        # Otherwise, check on left and right
        leftVal = self.bfs(root.left, target)
        
        # If the correct node is on left side
        if leftVal != -1: return leftVal
        
        rightVal = self.bfs(root.right, target)
        
        return rightVal
    
    def getTargetCopy(self, original, cloned, target):
        
        return self.bfs(cloned, target)

original = TreeNode(7)
original.left = TreeNode(4)
target = original.right = TreeNode(3)
original.right.left = TreeNode(6)
original.right.right = TreeNode(19)

cloned = TreeNode(7)
cloned.left = TreeNode(4)
cloned.right = TreeNode(3)
cloned.right.left = TreeNode(6)
cloned.right.right = TreeNode(19)

print("Output ->", Solution().getTargetCopy(original, cloned, target).val)

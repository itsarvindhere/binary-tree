class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def getTargetCopy(self, original, cloned, target):
        
        # Since "cloned" is a copy of "original"
        # It means, we can traverse both in the same manner
        # The advantage is that at any time, we can compare nodes as original == target
        # Because both belong to the same tree
        # This eliminates the need to worry about uniques or duplicate values in the tree
        # And if we found the "target" node in "original", then at the same point in cloned, we will get the same node
        # So, we can simply return that node 

        # BASE CASE
        if not original: return None
        
        # If current "original" node is same as "target"
        # Return the respective "cloned" node
        if original == target: return cloned
        
        # Check on left side
        leftVal = self.getTargetCopy(original.left, cloned.left, target)
        
        # If we found the target node on left side
        if leftVal: return leftVal
        
        # Check on right side
        rightVal = self.getTargetCopy(original.right, cloned.right, target)
        
        # Otherwise, return the rightVal (It is either the node, if found, or None)
        return rightVal

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

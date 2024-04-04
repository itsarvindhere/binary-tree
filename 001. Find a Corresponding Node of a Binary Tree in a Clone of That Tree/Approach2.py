class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    # Check if two trees are the same
    def isSameTree(self, p, q) -> bool:
        
        # If both or any one is null
        # If both are null, than p will be equal to q and in that case we will return True
        # But, if one is null and other is not, it means they are not equal to we will return False
        if not p or not q: return p == q
        
        # Two trees are same if the root node has same value
        # And the left and right subtrees are also same
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def getTargetCopy(self, original, cloned, target):
        
        # BASE CASE
        if not cloned or not target: return cloned if cloned == target else -1
        
        # If the node in "cloned" as same value as "target" node
        # This may or may not be the correct node (In case the values are not unique in the tree)
        if cloned.val == target.val:
            
            # Only if the subtrees are same, then we found the correct node to return
            if self.isSameTree(cloned, target): return cloned
            
            # Otherwise, it means the current "cloned" node is not the correct node to return
            return -1
        
        # If the current "cloned" node doesn't have the same value as target node
        # Check if the node matching the target node is on the left side
        leftVal = self.getTargetCopy(original, cloned.left, target)
        
        # If the node matching the target node is on the left side, return the node
        if leftVal != -1: return leftVal
        
        # Otherwise, check on the right side
        rightVal = self.getTargetCopy(original, cloned.right, target)
                                      
        # If the node matching the target node is on the left side, return the node
        if rightVal != -1: return rightVal
        
        # Otherwise, the current subtree does not have the node at all
        return -1

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

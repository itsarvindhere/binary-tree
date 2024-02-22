class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def isSameTree(self, p, q) -> bool:
        
        # BASE CASE
        # If both are null, than p will be equal to q and in that case we will return True
        # But, if one is null and other is not, it means they are not equal to we will return False
        if not p or not q: return p == q
        
        # Two trees are same if the root node has same value
        # And the left and right subtrees are also same
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print("Are two trees the same ->", Solution().isSameTree(p,q))
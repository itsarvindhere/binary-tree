# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper method to check if two trees are the same or not
    def isSameTree(self, p, q) -> bool:
        
        # If both or any one is null
        # If both are null, than p will be equal to q and in that case we will return True
        # But, if one is null and other is not, it means they are not equal to we will return False
        if not p or not q: return p == q
        
        # Two trees are same if the root node has same value
        # And the left and right subtrees are also same
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
    def isSubtree(self, root, subRoot) -> bool:
        
        # Base case
        if not root or not subRoot: return root == subRoot
        
        # If the trees with roots as "root" and "subRoot" are the same
        # Then, it means "subRoot" is a subtree of "root"
        if self.isSameTree(root, subRoot): return True
        
        # Otherwise, traverse left
        isSubtreeOnLeft = self.isSubtree(root.left, subRoot)
        
        # If the left traversal returns true, it means there exists a subtree that is same as "subRoot"
        # Hence, it means we can return True
        if isSubtreeOnLeft: return True
        
        # Traverse right
        isSubtreeOnRight = self.isSubtree(root.right, subRoot)
        
        # Return whatever the right traversal returns
        return isSubtreeOnRight


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)


subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print("Output -> ",Solution().isSubtree(root,subRoot))
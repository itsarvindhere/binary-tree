class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Preorder Traversal of a tree
    def preOrder(self, root, arr):
        
        # Base case
        if not root: 
            # Push "None" to the arr before returning
            arr.append(None)
            return
        
        # Put the root node's value in the arr
        arr.append(root.val)
        
        # Recursive Calls
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)
    
    def isSameTree(self, p, q) -> bool:
        
        # Get the preorder traversal of "p" and "q"
        pArr, qArr = [], []
        
        self.preOrder(p, pArr)
        self.preOrder(q, qArr)
        
        # Return True if both are equal
        return pArr == qArr

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print("Are two trees the same ->", Solution().isSameTree(p,q))
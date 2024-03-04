class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        
        # Stack with left and right children of root
        stack = [root.right, root.left]
        
        # While the stack is not empty
        while stack:
            
            # The top two nodes
            left, right = stack.pop(), stack.pop()
            
            # If both are Null, continue
            if not left and not right: continue
                
            # If one is null and other is not
            # Or if the values are not the same, then the tree is not symmetric
            if (not left or not right) or (left.val != right.val): return False
            
            
            # The mirror of the left node of "left" will be the right node of "right"
            # The mirror of the right node of "left" will be the left node of "right"
            
            # Push the right node of right tree then the left node of left tree
            stack.append(right.right)
            stack.append(left.left)
            
            # Push the left node of right tree then the right node of left tree
            stack.append(right.left)
            stack.append(left.right)
        
        # The tree is symmetric
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)

print("Is the Tree Symmetric? ", Solution().isSymmetric(root))

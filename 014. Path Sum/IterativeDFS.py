# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        
        # If the tree has no nodes
        if not root: return False
        
        # A Stack, initially with the root node and the target to find
        stack = [(root, targetSum)]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top of the stack along with the remaining target
            node, remainingTarget = stack.pop()
            
            # If the remainingTarget is same as current node's value and this is a leaf node
            # It means we found one valid path
            if not node.left and not node.right and remainingTarget == node.val: return True
            
            # Otherwise, push right child and left child to the stack
            if node.right: stack.append((node.right, remainingTarget - node.val))
            if node.left: stack.append((node.left, remainingTarget - node.val))
                
        # There exists no path that satisfies the criteria
        return False

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print("Output ->", Solution().hasPathSum(root, 22))
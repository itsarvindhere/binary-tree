class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def sumOfLeftLeaves(self, root):
        
        # Total Sum to return
        totalSum = 0
        
        # Stack, initialized with the root node and a flag to indicate if it is the left child
        stack = [(root, False)]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top of the stack, along with its flag
            node, isLeftNode = stack.pop()
            
            # If this is a leaf node and also a left leaf node
            if not node.left and not node.right and isLeftNode: totalSum += node.val
                
            # Push the right child in the stack
            if node.right: stack.append((node.right, False))
                
            # Push the left child in the stack
            if node.left: stack.append((node.left, True))
        
        # Return the total Sum
        return totalSum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Total Sum of Left Leaves -> ", Solution().sumOfLeftLeaves(root))
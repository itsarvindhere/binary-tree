
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def maxAncestorDiff(self, root) -> int:
        
        # Maximum difference to return
        maxDiff = 0
        
        # Stack, initially with the root node
        # The other two values indicate the minimum and maximum ancestor values so far (Initially, root values)
        stack = [[root, root.val, root.val]]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top of the stack along with other two values
            node, minAncestorValue, maxAncestorValue = stack.pop()
            
            # Update the maximum difference accordingly
            maxDiff = max(maxDiff, abs(node.val - minAncestorValue), abs(node.val - maxAncestorValue))
            
            # If there is a right child, push it to the stack
            if node.right: stack.append([node.right, min(minAncestorValue, node.val), max(maxAncestorValue, node.val)])
                
            # If there is a left child, push it to the stack
            if node.left: stack.append([node.left, min(minAncestorValue, node.val), max(maxAncestorValue, node.val)])
        
        # Return the maximum difference
        return maxDiff

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)
root.left.right.left = TreeNode(4)
root.right.right.right = TreeNode(7)

print("Output -> ", Solution().maxAncestorDiff(root))
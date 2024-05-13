# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def sumNumbers(self, root) -> int:
        
        # The total sum to return
        total = 0
        
        # A Stack, initially with the root node
        stack = [[root, 0]]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top
            node, numSoFar = stack.pop()
            
            # Update the number from root to current node
            numSoFar = (numSoFar * 10) + node.val
            
            # If this is a leaf node
            if not node.left and not node.right: total += numSoFar
            
            # If the node has a right child, push to the stack
            if node.right: stack.append([node.right, numSoFar])
                
            # If the node has a left child, push to the stack
            if node.left: stack.append([node.left, numSoFar])

        # Return the total sum
        return total

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print("Output -> ", Solution().sumNumbers(root))
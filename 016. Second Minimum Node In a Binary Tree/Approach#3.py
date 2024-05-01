from sortedcontainers import SortedSet
from math import inf
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def findSecondMinimumValue(self, root) -> int:
        
        # First & Second Minimum Values
        firstMinimum, secondMinimum = inf,inf
        
        # Stack
        stack = [root]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top of the stack
            node = stack.pop()
            
            # Update the minimum values
            if node.val < firstMinimum:
                secondMinimum = firstMinimum
                firstMinimum = node.val
            elif node.val != firstMinimum and node.val < secondMinimum: 
                secondMinimum = node.val
            
            # Put the right child in the stack
            if node.right: stack.append(node.right)
                
            # Put the left child in the stack
            if node.left: stack.append(node.left)
        
        # Return the second minimum value
        return secondMinimum if secondMinimum != inf else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Output -> ",Solution().findSecondMinimumValue(root))
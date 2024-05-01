from sortedcontainers import SortedSet
from math import inf
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # Traverse the tree to find the second minimum value
    def traverse(self, root, firstMinimum, secondMinimum):
        
        # Base Case
        if not root: return
        
        # Update the values
        if root.val < firstMinimum[0]:
            secondMinimum[0] = firstMinimum[0]
            firstMinimum[0] = root.val
        elif root.val != firstMinimum[0] and root.val < secondMinimum[0]: 
            secondMinimum[0] = root.val
            
        # Traverse left
        self.traverse(root.left, firstMinimum, secondMinimum)
        
        # Traverse right
        self.traverse(root.right, firstMinimum, secondMinimum)
    
    def findSecondMinimumValue(self, root) -> int:
        
        # First & Second Minimum Values
        firstMinimum, secondMinimum = [inf], [inf]
        
        # Call the helper function
        self.traverse(root, firstMinimum, secondMinimum)
        
        # Return the second minimum value
        return secondMinimum[0] if secondMinimum[0] != inf else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Output -> ",Solution().findSecondMinimumValue(root))
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
    def traverse(self, root, rootVal, secondMinimum):
        
        # Base Case
        if not root: return
        
        # Update the values
        if root.val > rootVal and root.val < secondMinimum[0]: secondMinimum[0] = root.val
            
        # No Need to further traverse if the current "root" has a value greater than the second smallest so far
        # Because, remember that any subRoot will have a value that is smaller out of its left and right children
        # So, if current subRoot has a value greater than second minimum we have found so far
        # It means, no other node under it can have a value smaller than the current second minimum we have found
        # So, it makes no sense to traverse further on this route
        if root.val > secondMinimum[0]: return
            
        # Traverse left
        self.traverse(root.left, rootVal, secondMinimum)
        
        # Traverse right
        self.traverse(root.right, rootVal, secondMinimum)
    
    def findSecondMinimumValue(self, root) -> int:
        
        # root value & Second Minimum Value
        rootVal, secondMinimum = root.val, [inf]
        
        # Call the helper function
        self.traverse(root, rootVal, secondMinimum)
        
        # Return the second minimum value
        return secondMinimum[0] if secondMinimum[0] != inf else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Output -> ",Solution().findSecondMinimumValue(root))
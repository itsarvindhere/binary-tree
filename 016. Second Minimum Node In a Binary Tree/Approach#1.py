from sortedcontainers import SortedSet

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # Traverse the tree and put the values in the sorted set
    def traverse(self, root, sortedSet):
        
        # Base Case
        if not root: return
        
        # Add the value in the Sorted Set
        sortedSet.add(root.val)
        
        # If the sorted set's length exceeds 2, pop the last value from it
        if len(sortedSet) > 2: sortedSet.pop(2)
            
        # Traverse left
        self.traverse(root.left, sortedSet)
        
        # Traverse right
        self.traverse(root.right, sortedSet)
    
    def findSecondMinimumValue(self, root) -> int:
        
        # Sorted Set
        sortedSet = SortedSet()
        
        # Call the helper function
        self.traverse(root, sortedSet)
        
        # Return the second minimum value
        return sortedSet[1] if len(sortedSet) > 1 else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Output -> ",Solution().findSecondMinimumValue(root))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive Function to get the sum
    def getSum(self, root, numSoFar, total):
        
        # Base Case
        if not root: return
        
        # Update the number from root to current node so far
        numSoFar = numSoFar * 10 + root.val
        
        # If this is a leaf node
        if not root.left and not root.right: total[0] += numSoFar
            
        # Recursive calls for left and right subtrees
        self.getSum(root.left, numSoFar, total)
        
        # Recursive calls for left and right subtrees
        self.getSum(root.right, numSoFar, total)
        
    
    def sumNumbers(self, root):
        
        # The total sum to return
        total = [0]
        
        # Call the recursive function to traverse the tree
        self.getSum(root, 0, total)
        
        # Return the total sum
        return total[0]

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print("Output -> ", Solution().sumNumbers(root))
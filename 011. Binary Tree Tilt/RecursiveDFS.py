# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
 
    # Helper function to find the total sum
    def dfs(self, root, total):
        
        # Base Case
        if not root: return 0
        
        # Get the sum of left subtree
        leftSubtreeSum = self.dfs(root.left, total)
        
        # Get the sum of right subtree
        rightSubtreeSum = self.dfs(root.right, total)
        
        # Calculate the tilt value for "root" node and add it to the total sum
        total[0] += abs(leftSubtreeSum - rightSubtreeSum)
        
        # Return the sum of current subtree back
        return leftSubtreeSum + rightSubtreeSum + root.val

    def findTilt(self, root):
        
        # Total sum of every list
        total = [0]
        
        # Call the recursive function
        self.dfs(root, total)
        
        # Return the sum
        return total[0]

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

print("Output -> ", Solution().findTilt(root))
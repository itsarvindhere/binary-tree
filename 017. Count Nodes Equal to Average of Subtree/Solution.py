# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function for traversal
    def traverse(self, root, count):
        
        # Base Case
        if not root: return [0,0]
        
        # Traverse left and get the total sum and count of nodes
        leftSum, leftCount = self.traverse(root.left, count)
        
        # Traverse right
        rightSum, rightCount = self.traverse(root.right, count)
        
        # Check the condition
        if (leftSum + root.val + rightSum) // (leftCount + 1 + rightCount) == root.val: count[0] += 1
            
        # Return the data for current subtree back
        return [leftSum + root.val + rightSum, leftCount + 1 + rightCount]
    
    
    def averageOfSubtree(self, root) -> int:
        
        # To keep track of the count of nodes
        count = [0]
        
        # Call the helper function
        self.traverse(root, count)
        
        # Return the count of nodes
        return count[0]

root = TreeNode(4)
root.left = TreeNode(8)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.right = TreeNode(6)

print("Output -> ", Solution().averageOfSubtree(root))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # Helper function to traverse the tree and get the total sum
    def getTotalSum(self, root, totalSum):
        
        # Base Case
        if not root: return
        
        # Add to the totalSum
        totalSum[0] += root.val
        
        # Traverse left
        self.getTotalSum(root.left, totalSum)
        
        # Traverse right
        self.getTotalSum(root.right, totalSum)
        
    # Helper function to get the maximum product
    def getMaxProduct(self, root, totalSum, maxProduct):
        
        # Base Case 
        if not root: return 0
        
        # Sum of left subtree
        leftSum = self.getMaxProduct(root.left, totalSum, maxProduct)
        
        # Sum of right subtree
        rightSum = self.getMaxProduct(root.right, totalSum, maxProduct)
        
        # Now, for the current node, we need to find which will give us the maximum product
        # Either we remove the left edge or the right edge
        product1, product2 = leftSum * (totalSum - leftSum), rightSum *(totalSum - rightSum)
                                                                        
        # So, get the highest among the two and update the maxProduct accordingly
        maxProduct[0] = max(maxProduct[0], product1, product2)
        
        # Return the sum for previous recursive calls
        return leftSum + root.val + rightSum
    
    def maxProduct(self, root) -> int:
        
        # Total Sum of nodes in a tree
        totalSum = [0]
        self.getTotalSum(root, totalSum)
        
        # Call the recursive function that finds the maximum product
        maxProduct = [1]
        self.getMaxProduct(root, totalSum[0], maxProduct)
        
        # Return the maximum product
        return maxProduct[0] % (10**9 + 7)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Output -> ", Solution().maxProduct(root))
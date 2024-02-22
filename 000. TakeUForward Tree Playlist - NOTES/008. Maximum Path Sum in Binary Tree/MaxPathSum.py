class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # A recursive function to get the maximum path sum 
    def getMaxPathSum(self,root, maxSum):
        
        # Base case
        if not root: return 0
        
        # Max path sum on left
        lSum = self.getMaxPathSum(root.left, maxSum)
        
        # Max path sum on right
        rSum = self.getMaxPathSum(root.right, maxSum)
        
        # Update the maxSum
        # It can be one of these path sums -
        # 1. left + root + right
        # 2. left + root
        # 3. right + root
        # 4. root
        maxSum[0] = max(maxSum[0], lSum + root.val + rSum, lSum + root.val, rSum + root.val, root.val)
        
        # What to return?
        # It is one of these three -
        # 1. left + root
        # 2. right + root
        # 3. root
        
        # You may argue that why not "left + root + right"?
        # Remember that this is a recursive function
        # It means, when this is returned, this result is then passed 
        # to the previous recursive call in the stack
        # And for that previous recursive call, new "root" will be a node that is parent of current "root"
        # And a path from that new "root", which goes through the current "root"
        # Simply cannot include both the left and right children of the current "root"
        # It is hard to explain like this, but here is a good visual explanation -> https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
        return max(lSum + root.val, rSum + root.val, root.val)

    def maxPathSum(self, root) -> int:
        
        # To keep track of the maximum path sum
        maxSum = [float("-inf")]
        
        # If there is no node
        if not root: return 0
        
        self.getMaxPathSum(root, maxSum)
        
        # Return the maximum path sum
        return maxSum[0]

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Maximum Path Sum -> ",Solution().maxPathSum(root));
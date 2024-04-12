class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Recursive DFS function
    def dfs(self, root, totalSum, isLeftNode):
        
        # Base Case
        if not root: return
        
        # If this is the leaf node and it is the left leaf node
        if not root.left and not root.right and isLeftNode: totalSum[0] += root.val
        
        # Traverse left
        self.dfs(root.left, totalSum, True)
        
        # Traverse right
        self.dfs(root.right, totalSum, False)

    
    def sumOfLeftLeaves(self, root):
        
        # Total Sum to return
        totalSum = [0]
        
        # Call the recursive DFS function
        self.dfs(root, totalSum, False)
        
        # Return the total Sum
        return totalSum[0]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Total Sum of Left Leaves -> ", Solution().sumOfLeftLeaves(root))
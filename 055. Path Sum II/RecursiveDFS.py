# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Traverse the tree to find all the valid paths
    def dfs(self, root, currPath, currPathSum, validPaths, targetSum):
        
        # Base Case
        if not root: return
        
        # Add to the current path list
        currPath.append(root.val)
        
        # Add to the current path sum
        currPathSum += root.val
        
        # If this is a leaf node
        if not root.left and not root.right:
            
            # If the path sum is equal to target, add current path to the list of valid paths
            if currPathSum == targetSum: validPaths.append(currPath[:])
                
        # Traverse left
        self.dfs(root.left, currPath, currPathSum, validPaths, targetSum)
        
        # Traverse right
        self.dfs(root.right, currPath, currPathSum, validPaths, targetSum)
        
        # Once we are done with the current node, we can remove it from the current path and also update currPathSum
        currPathSum -= currPath.pop()
    
    def pathSum(self, root, targetSum: int):
        
        # A list of all the valid paths
        validPaths = []
        
        # Call the DFS function
        self.dfs(root, [], 0, validPaths, targetSum)
        
        # Return the list
        return validPaths

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

targetSum = 22

print("Output -> ", Solution().pathSum(root, targetSum))
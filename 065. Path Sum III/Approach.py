# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Recursive DFS function to get the count of paths
    def dfs(self, root, targetSum, currSum, pathSums, count):
        
        # Base Case
        if not root: return
        
        # Update the currSum
        currSum += root.val
        
        # If the current path has a sum equal to target, update the count
        if currSum == targetSum: count[0] += 1
            
        # Otherwise, for the current path, 
        # can we exclude a path such that remaining path has sum equal to targetSum?
        # For that, we check our pathSums dictionary
        if currSum - targetSum in pathSums: count[0] += pathSums[currSum - targetSum]
            
        # Add to the dictionary
        pathSums[currSum] = pathSums.get(currSum, 0) + 1
            
        # Traverse left
        self.dfs(root.left, targetSum, currSum, pathSums, count)
        
        # Traverse right
        self.dfs(root.right, targetSum, currSum, pathSums, count)
        
        # Once we are done with left and right subtrees, remove the current path sum from the dictionary
        pathSums[currSum] -= 1
    
    def pathSum(self, root, targetSum: int) -> int:
        
        # To get the count of paths
        count = [0]
        
        # Call the recursive DFS function that will calculate the count of paths
        self.dfs(root, targetSum, 0, {}, count)
        
        # Return the count
        return count[0]
        

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
root.right.right = TreeNode(11)

targetSum = 8

print("Output -> ", Solution().pathSum(root, targetSum))
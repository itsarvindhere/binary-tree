# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ******************
# DFS APPROACH
# ******************
class Solution:
    
    # A Helper function to traverse the tree in DFS manner to get the sum of values in each level
    def getLevelSum(self, root, currLevel, levelSum):
        
        # Base Case
        if not root: return
        
        # Update the level sum for "currLevel"
        levelSum[currLevel] = levelSum.get(currLevel, 0) + root.val
        
        # Traverse left
        self.getLevelSum(root.left, currLevel + 1, levelSum)
        
        # Traverse right
        self.getLevelSum(root.right, currLevel + 1, levelSum)
        
        
    # A Helper function to traverse the tree in DFS manner and replace the node values accordingly
    def replace(self, root, siblingValue, currLevel, levelSum):
        
        # Base Case
        if not root: return
        
        # Replace the value
        root.val = levelSum[currLevel] - (root.val + siblingValue)
        
        # Values of siblings
        leftSiblingVal = root.left.val if root.left else 0
        rightSiblingVal = root.right.val if root.right else 0
        
        # Traverse left
        self.replace(root.left, rightSiblingVal, currLevel + 1, levelSum)
        
        # Traverse right
        self.replace(root.right, leftSiblingVal, currLevel + 1, levelSum)
        

    def replaceValueInTree(self, root):
        
        # A Dictionary to keep track of the level and sum of all the nodes at that level
        levelSum = {}
        
        # Call the helper function to get the level sum
        self.getLevelSum(root, 0, levelSum)
        
        # Call the helper function to replace the node values
        self.replace(root, 0, 0, levelSum)
        
        # Finally, return the root node after replacing the values of all the nodes correctly
        return root


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)

print("Output -> ", Solution().replaceValueInTree(root))
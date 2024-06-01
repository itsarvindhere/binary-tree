# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def pathSum(self, root, targetSum: int):
        
        # A list of all the valid paths
        validPaths = []
        
        # Stack, initially with root node and the path so far till the root (empty list) and path sum
        stack = []
        if root: stack.append([root, [], 0])
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top of the stack
            node, pathSoFar, pathSum = stack.pop()
            
            # Push the current node's value to the path so far
            pathSoFar.append(node.val)
            pathSum += node.val
            
            # If this is a leaf node, check if the path is valid
            if not node.left and not node.right and pathSum == targetSum: validPaths.append(pathSoFar)
            
            # If there is a right child, push to the stack
            if node.right: stack.append([node.right, pathSoFar[:], pathSum])
                
            # If there is a left child, push to the stack
            if node.left: stack.append([node.left, pathSoFar[:], pathSum])
        
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
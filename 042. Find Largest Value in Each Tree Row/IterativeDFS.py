# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def largestValues(self, root):
        
        # Output list to return
        output = []
        
        # If there is no tree
        if not root: return output
        
        # A dictionary to keep track of the level and the maximum value at that level
        maxValues = {}
        
        # A Stack, initially with the root node, and the level
        stack = [[root, 0]]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top
            node, level = stack.pop()
            
            # Update the maximum for the current level
            if level in maxValues: maxValues[level] = max(maxValues[level], node.val)
            else: maxValues[level] = node.val
            
            # If the node has a right child, push to the stack
            if node.right: stack.append([node.right, level + 1])
                
            # If the node has a left child, push to the stack
            if node.left: stack.append([node.left, level + 1])
        
        # Iterate over the dictionary and put the maximum values for each level in the output list
        for level in maxValues: output.append(maxValues[level])
        
        # Finally, return the output list
        return output
                
                

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

print("Output -> ", Solution().largestValues(root))
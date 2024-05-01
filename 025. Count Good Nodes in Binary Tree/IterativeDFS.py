
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    
    def goodNodes(self, root) -> int:
        
        # Count of good nodes
        count = 0
        
        # Stack, initially with the root node and the maximum on current path so far
        stack = [[root, root.val]]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top of the stack
            node, maxSoFar = stack.pop()
            
            # If the node has a value >= maxSoFar, then it is a good node
            if node.val >= maxSoFar: 
                count += 1
                maxSoFar = node.val
                
            # If the node has a right child, push it to the stack
            if node.right: stack.append([node.right, maxSoFar])
                
            # If the node has a left child, push it to the stack
            if node.left: stack.append([node.left, maxSoFar])
        
        # Return the count
        return count

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print("Output -> ", Solution().goodNodes(root))
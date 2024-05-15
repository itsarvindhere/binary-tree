# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Recursive DFS function
    def dfs(self, root, val, currDepth, depth):
        
        # Base Case
        if not root or currDepth >= depth: return
        
        # If the current depth is "depth - 1"
        if currDepth == depth - 1:
            prevLeft, prevRight = root.left, root.right
            
            # Create two nodes with values = val as the left and right child
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            
            # Join the nodes accordingly
            root.left.left = prevLeft
            root.right.right = prevRight
        
        # Traverse left
        self.dfs(root.left, val, currDepth + 1, depth)
        
        # Traverse right
        self.dfs(root.right, val, currDepth + 1, depth)
    
    
    def addOneRow(self, root, val, depth):
        
        # If depth = 1
        if depth == 1: 
            node = TreeNode(val)
            node.left = root
            return node
        
        
        # DFS Function to traverse the tree
        self.dfs(root, val, 1, depth)
        
        # Return the root node after adding the row
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

val = 1
depth = 2

print("Output -> ", Solution().addOneRow(root, val, depth))
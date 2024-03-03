from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Pre-Order Traversal
    def preOrder(self, root, level, nodesMap, levels):
        
        # Base case
        if not root: return
        
        # Update the leftmost node for current level
        if level not in nodesMap: nodesMap[level] = root.val
        
        # Update levels
        levels[0] = max(levels[0], level)
        
        # Traverse left
        self.preOrder(root.left, level + 1, nodesMap, levels)
        
        # Traverse right
        self.preOrder(root.right, level + 1, nodesMap, levels)
    
    
    def leftSideView(self, root):
        
        # Output list to return
        output = []
        
        # Dictionary to keep the "level" and the leftmost node in that level
        nodesMap = {}
        
        # If there is no node
        if not root: return output
        
        # How many levels are there
        levels = [0]
        
        # Pre-Order Traversal
        self.preOrder(root, 0, nodesMap, levels)
        
        # Go over each level and put the leftmost node at that level in the output list
        for i in range(levels[0] + 1): output.append(nodesMap[i])
        
        # Finally, return the output list
        return output

root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(1)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)

print("Output -> ", Solution().leftSideView(root))
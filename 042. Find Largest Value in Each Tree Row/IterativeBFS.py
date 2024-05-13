from collections import deque
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        
        # The output list
        output = []
        
        # If there is no tree at all
        if not root: return output
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Maximum in current row
            maxInCurrRow = -inf
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Update the maximum
                maxInCurrRow = max(maxInCurrRow, node.val)
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1
                
            # Push the maximum for the current row in the output list
            output.append(maxInCurrRow)
            
        # Finally, return the output list
        return output

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

print("Output -> ", Solution().largestValues(root))
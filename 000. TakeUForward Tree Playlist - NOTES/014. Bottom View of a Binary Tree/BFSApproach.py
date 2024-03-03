class TreeNode:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

from collections import deque
import math
class Solution:
    
    #Function to return a list of nodes visible from the bottom view 
    #from left to right in Binary Tree.
    def bottomView(self,root):
        
        # code here
        # Output list to return
        output = []
        
        # A dictionary to keep track of the column number and the first node in that column
        nodesMap = {}

        # Queue
        queue = deque()
        
        # Let's consider the root node at row 0 and column 0
        # We will push the root node along with its column value
        queue.append([root, 0])
        
        # To keep track of the minimum and maximum column numbers
        minC, maxC = math.inf, -math.inf
        
        # Level Order Traversal
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            while nodesInCurrentLevel > 0:
                
                # Pop from the queue
                node,colNumber = queue.popleft()
                
                # Update the minimum and maximum column values
                minC = min(minC, colNumber)
                maxC = max(maxC, colNumber)
                
                # Update the dictionary accordingly
                nodesMap[colNumber] = node.data
                
                # If the node has a left child, push to the queue
                if node.left: queue.append([node.left, colNumber - 1])
                 
                # If the node has a right child, push to the queue
                if node.right: queue.append([node.right, colNumber + 1])
                
                # Update the count of nodes in current level
                nodesInCurrentLevel -= 1
                
        for col in range(minC, maxC + 1): output.append(nodesMap[col])
            
        # Return the output list
        return output


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

root.right = TreeNode(3)
root.right.right = TreeNode(7)

print("Output -> ", Solution().bottomView(root))
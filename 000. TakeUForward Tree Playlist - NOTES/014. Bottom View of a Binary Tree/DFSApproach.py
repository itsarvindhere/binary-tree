class TreeNode:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

from collections import deque
import math
class Solution:
    
    
    # Pre Order Traversal
    def preOrder(self, root, colNumber, rowNumber, nodesMap, minMax):
        
        # Base case
        if not root: return
    
        # Put the root node's value in the dictionary if colNumber doesn't already exist
        # If the colNumber exist but the root node is at a lower or equal level, then replace it
        if colNumber not in nodesMap or nodesMap[colNumber][1] <= rowNumber: nodesMap[colNumber] = [root.data,rowNumber]
        
        # Update the minimum and maximum column numbers
        minMax[0] = min(minMax[0], colNumber)
        minMax[1] = max(minMax[1], colNumber)
        
        # Traverse left
        self.preOrder(root.left, colNumber - 1, rowNumber + 1, nodesMap, minMax)
        
        # Traverse Right
        self.preOrder(root.right, colNumber + 1, rowNumber + 1, nodesMap, minMax)
    
    
    
    #Function to return a list of nodes visible from the bottom view 
    #from left to right in Binary Tree.
    def bottomView(self,root):

        output = []
        
        # A dictionary to keep track of the column number and the first node in that column
        nodesMap = {}

        # Queue
        queue = deque()
        
        # Let's consider the root node at row 0 and column 0
        # We will push the root node along with its column value
        queue.append([root, 0])
        
        # To keep track of the minimum and maximum column numbers
        minMax = [math.inf, -math.inf]
        
        # Recursive Pre-Order Function
        self.preOrder(root, 0, 0, nodesMap, minMax)
        
        minC,maxC = minMax
        for col in range(minC, maxC + 1): output.append(nodesMap[col][0])
            
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
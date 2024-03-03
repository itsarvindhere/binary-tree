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
        # If the colNumber exist but the root node is at a higher level, then replace it
        if colNumber not in nodesMap or nodesMap[colNumber][1] > rowNumber: nodesMap[colNumber] = [root.data,rowNumber]
        
        # Update the minimum and maximum column numbers
        minMax[0] = min(minMax[0], colNumber)
        minMax[1] = max(minMax[1], colNumber)
        
        # Traverse left
        self.preOrder(root.left, colNumber - 1, rowNumber + 1, nodesMap, minMax)
        
        # Traverse Right
        self.preOrder(root.right, colNumber + 1, rowNumber + 1, nodesMap, minMax)
    
    
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):

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


root = TreeNode(10)
root.left = TreeNode(20)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.left.left = TreeNode(70)
root.left.left.right = TreeNode(80)

root.right = TreeNode(30)
root.right.right = TreeNode(60)
root.right.right.right = TreeNode(90)

print("Output -> ", Solution().topView(root))
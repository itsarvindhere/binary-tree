from collections import defaultdict, deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Pre Order Traversal
    def preOrder(self, root, nodesMap, row, col, triplet):
        
        # Base case
        if not root: return
        
        # Update rows count
        triplet[0] += 1
        
        # Get the root node and put its value in dictionary
        nodesMap[(row,col)].append(root.val)
        
        # Update minimum and maximum column values
        triplet[1] = min(triplet[1], col)
        triplet[2] = max(triplet[2], col)
        
        # Traverse left
        self.preOrder(root.left, nodesMap, row + 1, col - 1, triplet)
        
        # Traverse right
        self.preOrder(root.right, nodesMap, row + 1, col + 1, triplet)
    
    def verticalTraversal(self, root):
        
        # A hashtable to keep track of the nodes at each (row, col)
        nodesMap = defaultdict(list)
        
        # Number of rows, Minimum column number and maximum column number
        triplet = [-1, inf, -inf]
        
        # Pre Order Traversal
        self.preOrder(root, nodesMap, 0, 0, triplet)
        
        # Output List to return
        output = []
        
        row,minC,maxC = triplet
                
        # Go over each column
        for i in range(minC, maxC + 1):
            
            # Sublist for each column
            colList = []
            
            # Go over each row
            for j in range(row + 1):
                
                # Take the nodes at (row,col) and push them in sorted order in the colList
                if (j,i) in nodesMap: colList += sorted(nodesMap[(j,i)])
            
            # Push the sublist to the output list
            if colList: output.append(colList)
                
        # Return the output list
        return output


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Output -> ", Solution().verticalTraversal(root))
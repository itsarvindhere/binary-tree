from collections import defaultdict, deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):
        
        # A hashtable to keep track of the nodes at each (row, col)
        nodesMap = defaultdict(list)
        
        # Queue
        queue = deque()
        
        # Put the root node in the queue along with its column
        # The root node is at column "0"
        queue.append([root, 0])
        
        # To keep track of the row/level
        row = -1
        
        # Minimum and maximum column value
        minC, maxC = inf, -inf
        
        # While the queue is not empty
        while queue:
            
            # Update the row/level
            row += 1
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            while nodesInCurrentLevel > 0:
                
                # Remove the node in front of the queue
                node, col = queue.popleft()
                
                # Update max and min column values accordingly
                minC = min(minC, col)
                maxC = max(maxC, col)
                
                # Update the dictionary
                nodesMap[(row, col)].append(node.val)
                
                # If the node has a left child
                if node.left: queue.append([node.left, col - 1])
                    
                # If the node has a right child
                if node.right: queue.append([node.right, col + 1])
                    
                # Update the count of nodes in current level
                nodesInCurrentLevel -= 1
                
        # Output list to return
        output = []
        
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
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to get the height of the tree
    def getHeight(self, root):
        
        # Base Case
        if not root: return 0
        
        # Left Height
        leftHeight = self.getHeight(root.left)
        
        # Right Height
        rightHeight = self.getHeight(root.right)
        
        # Return the height
        return max(leftHeight, rightHeight) + 1
    
    def printTree(self, root):
        
        height = self.getHeight(root) - 1
        
        # Number of rows
        m = height + 1
        
        # Number of columns
        n = (2**(height + 1)) - 1
        
        # Create an output 2D matrix with m rows and n columns, initially with ""
        output = [[""] * n for i in range(m)]
        
        # Traverse the tree in BFS manner and put the values in the output list
        queue = deque()
        
        # We will push a triplet to the queue where the first value is the "node" itself
        # The second value is the "row" and the third value is the "column"
        queue.append([root, 0, n // 2])
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node,r,c = queue.popleft()
                
                # Push the value in the output list
                output[r][c] = str(node.val)
                
                # If the node has a left child
                if node.left: queue.append([node.left, r + 1,(c - (2**(height - r - 1)))])
                
                # If the node has a right child
                if node.right: queue.append([node.right, r + 1,(c + (2**(height - r - 1)))])
                
                # Update the count
                nodesInCurrentLevel -= 1
        
        # Return the output list
        return output

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print("Output ->", Solution().printTree(root))
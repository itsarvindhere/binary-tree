
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        
        # Queue
        queue = deque()
        
        # Initialize with root node
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.pop()
                
                # Data value for left and right child
                left,right = 0,0
                
                if node.left: 
                    queue.append(node.left)
                    left = node.left.val
                    
                if node.right: 
                    queue.append(node.right)
                    right = node.right.val
                    
                # If node has at least one child, check if it follows the children sum property
                if (left > 0 or right > 0) and node.val != left + right: return 0

                # Update the count
                nodesInCurrentLevel -= 1
                
        # The tree follows the Children Sum Property
        return 1


root = TreeNode(45)
root.left = TreeNode(35)
root.right = TreeNode(10)
root.left.left = TreeNode(30)
root.left.right = TreeNode(5)
root.right.left = TreeNode(8)
root.right.right = TreeNode(2)

print("Output -> ", Solution().isSumProperty(root))
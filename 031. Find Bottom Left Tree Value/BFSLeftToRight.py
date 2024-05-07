from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ******************************
# BFS SOLUTION - LEFT TO RIGHT
# ******************************
class Solution:
    def findBottomLeftValue(self, root) -> int:
        
        # Queue
        queue = deque()
        
        # Put the root node in the queue initially
        queue.append(root)
        
        # Initialize the bottom left value as root
        bottomLeftVal = root.val
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in current level
            currLevelNodes = len(queue)
            
            # Update the bottom left value as the value of leftmost node in current level
            bottomLeftVal = queue[0].val
            
            # Iterate over the current level nodes
            while currLevelNodes > 0:
                
                # Pop the node in front
                node = queue.popleft()
                
                # If there exists a left child, put it in the queue
                if node.left: queue.append(node.left)
                    
                # If there exists a right child, put it in the queue
                if node.right: queue.append(node.right)
                    
                # Update the number of nodes in current level
                currLevelNodes -= 1
                
        # Finally, return the bottom left node's value
        return bottomLeftVal

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)

print("Leftmost node in last level ->", Solution().findBottomLeftValue(root))
from sortedcontainers import SortedSet
from math import inf
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def findSecondMinimumValue(self, root) -> int:
        
        # First & Second Minimum Values
        firstMinimum, secondMinimum = inf,inf
        
        # Queue
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
            
                # Pop the node in front of the queue
                node = queue.popleft()

                # Update the minimum values
                if node.val < firstMinimum:
                    secondMinimum = firstMinimum
                    firstMinimum = node.val
                elif node.val != firstMinimum and node.val < secondMinimum: 
                    secondMinimum = node.val

                # Put the left child in the queue
                if node.right: queue.append(node.left)

                # Put the right child in the queue
                if node.left: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1
        
        # Return the second minimum value
        return secondMinimum if secondMinimum != inf else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Output -> ",Solution().findSecondMinimumValue(root))
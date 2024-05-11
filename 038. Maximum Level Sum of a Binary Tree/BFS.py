from collections import deque
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        
        # To keep track of the maximum level sum
        maxSum = -inf
        
        # To keep track of the level with the maximum sum
        maxSumLevel = -1
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # To keep track of the level
        level = 0
        
        # While the queue is not empty
        while queue:
            
            # Update the level
            level += 1
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Sum of current level
            currLevelSum = 0
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Update the sum of current level
                currLevelSum += node.val
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
            # Update the max sum level accordingly
            if currLevelSum > maxSum:
                maxSum = currLevelSum
                maxSumLevel = level
                
        # Finally, return the level with the maximum sum
        return maxSumLevel

root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

print("Output -> ", Solution().maxLevelSum(root))
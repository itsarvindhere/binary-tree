from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        
        # To keep the average of levels
        average = []
        
        # Queue
        queue = deque()
        
        # Push the root node
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            # Denominator for average
            denominator = nodesInCurrentLevel
            
            # Numerator (Sum of values of all nodes in current level)
            numerator = 0
            
            # Iterate over all nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Update the sum
                numerator += node.val
                
                # If the node has a left child
                if node.left: queue.append(node.left)
                    
                # If the node has a right child
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
            # Update the list
            average.append(numerator/denominator)
            
        # Return the output list
        return average


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Averages are -> ", Solution().averageOfLevels(root))
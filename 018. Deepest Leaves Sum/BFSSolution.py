from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root) -> int:
        
        # Sum of deepest leaves
        totalSum = 0
        
        # Queue
        queue = deque()
        queue.append(root)
        
        # While the queue in not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Reset the total sum because we want the sum of nodes in the last level
            totalSum = 0
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Add to the total sum
                totalSum += node.val
                
                # Push the left child in the queue
                if node.left: queue.append(node.left)
                    
                # Push the right child in the queue
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
            
        # Finally, return the sum of deepest leaves
        return totalSum

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)

print("Output -> ",Solution().deepestLeavesSum(root))
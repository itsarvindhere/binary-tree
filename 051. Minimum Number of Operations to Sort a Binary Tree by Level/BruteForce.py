from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root) -> int:
        
        # Minimum operations
        minOperations = 0
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Get the value of the nodes in the current level
            currLevelNodes = []
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                currLevelNodes.append(node.val)
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1
                
            # Find the minimum operations needed
            for i in range(len(currLevelNodes)):
                
                smallestIdx = i
                
                for j in range(i + 1, len(currLevelNodes)):
                    
                    if currLevelNodes[j] < currLevelNodes[smallestIdx]: smallestIdx = j
                        
                if smallestIdx != i: 
                    currLevelNodes[i], currLevelNodes[smallestIdx] = currLevelNodes[smallestIdx], currLevelNodes[i]
                    minOperations += 1
                
        # Return the minimum operations to sort each level
        return minOperations

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right.left = TreeNode(8)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(9)
root.right.right.left = TreeNode(10)

print("Output -> ", Solution().minimumOperations(root))
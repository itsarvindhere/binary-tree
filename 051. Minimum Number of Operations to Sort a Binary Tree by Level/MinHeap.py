from collections import deque
from heapq import heappush, heappop
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
            
            # To keep track of the index and the value at that index
            values = {}
            
            # Index of node values
            i = 0
            
            # A Min Heap
            minHeap = []
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                values[i] = node.val
                heappush(minHeap, [node.val, i])
                i += 1
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1
                
            # Find the minimum operations needed
            for i in values:
                
                # Remove outdated values from the minHeap
                while minHeap and values[minHeap[0][1]] != minHeap[0][0]: heappop(minHeap)
                
                # At this point, the top of the minHeap has the smallest value on the right of index "i"
                smallestIdx = heappop(minHeap)[1]
                        
                # If this is not the same index
                if smallestIdx != i:
                    
                    # Swap the values
                    values[i], values[smallestIdx] = values[smallestIdx], values[i]
                    
                    # Make sure to push the updated data in the minHeap
                    # We only need to push the data for the "smallestIdx"
                    # Because we have already placed correct value at index "i"
                    # So, the value at index "i" won't ever need to be changed
                    heappush(minHeap, [values[smallestIdx], smallestIdx])
                    
                    # Update the count of operations
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
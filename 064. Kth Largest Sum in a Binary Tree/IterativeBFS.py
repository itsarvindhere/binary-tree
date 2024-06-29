from collections import deque
from heapq import heappush, heappop

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # A Min Heap
        minHeap = []
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Sum of the current level
            currSum = 0
            
            # Iterate over all the nodes in current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front
                node = queue.popleft()
                
                # Update the current level's sum
                currSum += node.val
                
                # If there is a left child, push to the queue
                if node.left: queue.append(node.left)
                    
                # If there is a right child, push to the queue
                if node.right: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1
                
            # Push to the heap
            heappush(minHeap, currSum)
            
            # If the heap size exceeds k, pop the top
            if len(minHeap) > k: heappop(minHeap)
                
        # Return the kth largest level sum if there are at least "k" levels
        return minHeap[-0] if len(minHeap) == k else -1

root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)

k = 2

print("Output -> ", Solution().kthLargestLevelSum(root, k))
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def sumNumbers(self, root) -> int:
        
        # The total sum to return
        total = 0
        
        # A Queue, initially with the root node
        queue = deque()
        queue.append([root, 0])
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue, along with number so far
                node, numSoFar = queue.popleft()

                # Update the number from root to current node
                numSoFar = (numSoFar * 10) + node.val

                # If this is a leaf node
                if not node.left and not node.right: total += numSoFar

                # If the node has a left child, push to the queue
                if node.right: queue.append([node.right, numSoFar])

                # If the node has a right child, push to the queue
                if node.left: queue.append([node.left, numSoFar])
                    
                # Update the node count
                nodesInCurrentLevel -= 1

        # Return the total sum
        return total

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

print("Output -> ", Solution().sumNumbers(root))
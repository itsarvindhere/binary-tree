from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def pathSum(self, root, targetSum: int):
        
        # A list of all the valid paths
        validPaths = []
        
        # Queue, initially with root node and the path so far till the root (empty list) and path sum
        queue = deque()
        if root: queue.append([root, [], 0])
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node, pathSoFar, pathSum = queue.popleft()

                # Push the current node's value to the path so far
                pathSoFar.append(node.val)
                pathSum += node.val

                # If this is a leaf node, check if the path is valid
                if not node.left and not node.right and pathSum == targetSum: validPaths.append(pathSoFar)

                # If there is a left child, push to the queue
                if node.right: queue.append([node.right, pathSoFar[:], pathSum])

                # If there is a right child, push to the queue
                if node.left: queue.append([node.left, pathSoFar[:], pathSum])
                
                # Update the count
                nodesInCurrentLevel -= 1
        
        # Return the list
        return validPaths

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

targetSum = 22

print("Output -> ", Solution().pathSum(root, targetSum))
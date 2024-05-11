from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ******************
# BFS APPROACH
# ******************
class Solution:
    
    # A Helper function to traverse the tree in BFS manner to get the sum of values in each level
    def getLevelSum(self, root, levelSum):
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # Level
        level = -1
        
        # While the queue is not empty
        while queue:
            
            # Update the level
            level += 1
            
            # Count of nodes in the current level
            nodesInCurrentLevel = len(queue)
            
            # Sum of current level
            currLevelSum = 0
            
            # Iterate over all the nodes and get the sum
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
                
            # Update the dictionary
            levelSum[level] = currLevelSum
    
    
    
    def replaceValueInTree(self, root):
        
        # A Dictionary to keep track of the level and sum of all the nodes at that level
        levelSum = {}
        
        # Call the helper function to get the level sum
        self.getLevelSum(root, levelSum)
        
        # Traverse the tree in BFS order
        queue = deque()
        
        # The first value is the node, and second value is the sibling's value
        queue.append([root, 0])
        
        # To keep track of the level
        level = -1
        
        # While the queue is not empty
        while queue:
            
            # Update the level
            level += 1
            
            # Count of nodes in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue, along with its parent
                node, siblingValue = queue.popleft()
                
                # We need to replace the value of "node" with the sum of its cousin nodes
                # For any node, Sum of cousins = Total Sum of that level - (value of itself + its sibling)
                node.val = levelSum[level] - (node.val + siblingValue)
                
                # If the node has a left child, push it to the queue
                if node.left: queue.append([node.left, node.right.val if node.right else 0])
                    
                # If the node has a right child, push it to the queue
                if node.right: queue.append([node.right, node.left.val if node.left else 0])
                
                # Update the count
                nodesInCurrentLevel -= 1
        
        return root


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)

print("Output -> ", Solution().replaceValueInTree(root))
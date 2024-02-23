from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        
        # Output list to return
        output = []
        
        # If there is no node
        if not root: return output
        
        # Queue
        queue = deque()
        
        # Push the root node first
        queue.append(root)
        
        # To keep track of traversal order
        leftToRight = True
        
        # While queue is not empty
        while queue:
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            # Current level's nodes
            currLevelNodes = [0] * nodesInCurrentLevel
            
            # Pointer to keep track of the index at which we have to put the node in "currLevelNodes"
            i = 0 if leftToRight else nodesInCurrentLevel - 1
            
            while nodesInCurrentLevel > 0:
                
                # Pop the node from queue's front
                node = queue.popleft()
                
                # Put the node's value at correct position
                currLevelNodes[i] = node.val
                
                # Push the left and right children in the queue, if they exist
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
                # Update "i"
                i = i + 1 if leftToRight else i - 1
                
            # Update the order for next iteration
            leftToRight = not leftToRight
                
            # Update the output list
            output.append(currLevelNodes)
            
        # Finally, return the output list
        return output


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Result of Zig Zag Traversal ->", Solution().zigzagLevelOrder(root))
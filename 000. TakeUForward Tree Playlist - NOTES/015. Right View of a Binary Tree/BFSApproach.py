from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        
        # QUEUE
        queue = deque()
        
        # Output list to return
        output = []
        
        # If there is no node
        if not root: return output
        
        # Put the root node in the queue
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Rightmost node's value in current level
            rightmostNodeValue = -1
            
            while nodesInCurrentLevel > 0:
                
                # Pop the front node
                node = queue.popleft()
                
                # Update the rightmost node value for current level
                rightmostNodeValue = node.val
                
                # Push left and right child in the queue if they exist
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
                # Update the count of nodes in current level
                nodesInCurrentLevel -= 1
                
            # Push the rightmost node value in the output list
            output.append(rightmostNodeValue)
        
        # Finally, return the output list
        return output

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print("Output -> ", Solution().rightSideView(root))
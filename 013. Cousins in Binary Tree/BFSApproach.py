from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        
        # Queue
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Flags to check if "x" and "y" are in current level or not
            isXFound, isYFound = False, False
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the front node
                node = queue.popleft()
                
                # If the node has left and right children, make sure they both are not "x" and "y"
                # Because in that case, the nodes "x" and "y" won't be cousins
                if node.left and node.right:
                    
                    if node.left.val == x and node.right.val == y: return False
                    
                    elif node.left.val == y and node.right.val == x: return False
                
                # Update the flags accordingly
                if node.val == x: isXFound = True
                if node.val == y: isYFound = True
                    
                # If there is a left child, push it to the queue
                if node.left: queue.append(node.left)
                    
                # If there is a right child, push it to the queue
                if node.right: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
                
            # If we found both the nodes at current level, then they are cousins
            if isXFound and isYFound: return True
                
        # The nodes "x" and "y" are not cousins
        return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

x = 4
y = 3

print("Output -> ", Solution().isCousins(root, x, y))
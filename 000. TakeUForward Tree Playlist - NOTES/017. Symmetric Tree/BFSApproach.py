from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        
        # Queue
        queue = deque()
        
        # Put the left and right children of the root node in the queue
        # The second value indicates whether a node is the "left" child or "right" child
        queue.append(root.left)
        queue.append(root.right)
        
        # To keep track of the level
        level = 0
        
        # While the queue is not empty
        while queue:
            
            # Update the level
            level += 1
            
            # How many nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Half
            half = nodesInCurrentLevel // 2
            
            # A stack for the Node values in current level till the center of the level
            nodesTillHalf = []
            
            while nodesInCurrentLevel > 0:
                
                # Pop the front node along with its flag that indicates if it is left child or right child
                node = queue.popleft()
                
                # If the node count is <= half, compare
                if nodesInCurrentLevel <= half:
                    valOnTop = nodesTillHalf.pop()
                    
                    # A symmetric tree needs to have nodes values at opposite ends the same
                    # Moreover, if node on left of center line is a left child
                    # It should be a right child on the right of center line
                    # If any one of these two conditions is not satisfied, then tree is not symmetric
                    if (node.val if node else "N") != valOnTop: return False
                # Otherwise, push it to the stack
                else:
                    
                    # If a node is "None", push "N" as its value
                    nodesTillHalf.append(node.val if node else "N")
                    
                
                # If node is not "None"
                if node:
                    
                    # Push left child to the queue, doesn't matter if it exist or not
                    queue.append(node.left)

                    # Push right child to the queue, , doesn't matter if it exist or not
                    queue.append(node.right)
                    
                # Update the count of nodes in current level
                nodesInCurrentLevel -= 1
                
        # The tree is symmetric
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)

print("Is the Tree Symmetric? ", Solution().isSymmetric(root))

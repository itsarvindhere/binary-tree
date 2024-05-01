from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    
    # Helper function for BFS traversal
    def bfs(self, root, values):
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Update the values set
                values.add(node.val)
                
                # If there is a left child, push to the queue
                if node.left:
                    queue.append(node.left)
                    node.left.val = (2 * node.val) + 1
                
                # If there is a right child, push to the queue
                if node.right:
                    queue.append(node.right)
                    node.right.val = (2 * node.val) + 2
                    
                # Update the count
                nodesInCurrentLevel -= 1
            
    def __init__(self, root):
        
        # A set of values
        self.values = set()
        
        # Traverse the tree in BFS order
        # Update the root node's value to 0
        root.val = 0
        self.bfs(root, self.values)
        

    def find(self, target: int) -> bool:
        
        # Return true if the "target" exists in the set
        return target in self.values


root = TreeNode(-1)
root.right = TreeNode(-1)
findElements = FindElements(root); 

print(findElements.find(1))
print(findElements.find(2))
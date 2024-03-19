from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root, start: int) -> int:
        
        # First, for each node, we will keep track of what is the parent node
        # Since we have to traverse in all the directions from the infected node
        # That is, towards top, left and right
        parentNodes = {}
        
        # Queue for BFS
        queue = deque()
        queue.append(root)
        
        # The node from which the infection starts
        startNode = None
        
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If this is the target node, update the startNode
                if node.val == start: startNode = node
                    
                # If the node has a left child
                if node.left:
                    
                    # Update the dictionary
                    parentNodes[node.left] = node
                    
                    # Add to the queue
                    queue.append(node.left)
                    
                # If the node has a right child
                if node.right:
                    
                    # Update the dictionary
                    parentNodes[node.right] = node
                    
                    # Add to the queue
                    queue.append(node.right)
                    
                # Update the node count
                nodesInCurrentLevel -= 1
                
        # At this point, we know for each node, what is the parent node
        # So now, we can start the traversal from the startNode and check how many minutes are needed for entire tree to be infected
        queue = deque()
        queue.append(startNode)
        
        # To keep track of the minutes
        minutes = -1
        
        # To keep track of visited nodes. In other words, the nodes that are already infected
        visited = set()
        
        while queue:
            
            # Update the minutes
            minutes += 1
            
            # How many nodes are in the queue
            nodesInQueue = len(queue)
            
            while nodesInQueue > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Mark it as visited
                visited.add(node)
                
                # If the parent node is not already visited, put it in the queue
                if node in parentNodes and parentNodes[node] not in visited:
                    
                    # Add to the visited set
                    visited.add(parentNodes[node])
                    
                    # Add to the queue
                    queue.append(parentNodes[node])
                    
                # If the left child is not already visited, put it in the queue
                if node.left and node.left not in visited:
                    
                    # Add to the visited set
                    visited.add(node.left)
                    
                    # Add to the queue
                    queue.append(node.left)
                    
                # If the right child is not already visited, put it in the queue
                if node.right and node.right not in visited:
                    
                    # Add to the visited set
                    visited.add(node.right)
                    
                    # Add to the queue
                    queue.append(node.right)
                
                
                # Update the count
                nodesInQueue -= 1
            
            
        # Return the minutes
        return minutes


root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(2)

print("Output -> ", Solution().amountOfTime(root,3))
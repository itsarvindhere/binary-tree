from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        
        # A Dictionary to keep the parent nodes of every node in the Tree
        # This will be useful when from any node, we have to traverse towards top
        # Because in a Binary Tree, we can easily traverse top to bottom from any node
        # But not from bottom to top because a node does not contain any data about who the parent is
        # Only from the parent we can know who the children are
        parentNodes = {}
        
        # Queue, initially with the root node
        queue = deque()
        queue.append(root)
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # If the node has a left child
                if node.left:
                    
                    # Update the dictionary
                    parentNodes[node.left] = node
                    
                    # Push to the queue
                    queue.append(node.left)
                    
                # If the node has a right child
                if node.right:
                    
                    # Update the dictionary
                    parentNodes[node.right] = node
                    
                    # Push to the queue
                    queue.append(node.right)
                    
                
                # Update the count
                nodesInCurrentLevel -= 1
                
        # At this point, we know for each node, what is the parent
        # Now, from the "target" node, we start traversing outwards
        # That is, we traverse top, left and right at the same time
        
        # Queue, initially with the target node
        queue = deque()
        queue.append(target)
        
        # To keep track of visited nodes, initially with the target node
        visited = set()
        visited.add(target)
        
        # While we are not at a distance k from target
        while k > 0:
            
            # How many nodes are in the queue at this point
            # At any time, all nodes in the queue will be at the same distance from target
            nodesInQueue = len(queue)
            
            while nodesInQueue > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Now, we traverse outwards from this node. That is, towards top, left and right
                # The node on top is its parent (except if it is the root node)
                # If we haven't yet visited the parent node
                if node in parentNodes and parentNodes[node] not in visited:
                    
                    # Put the node in the visited set
                    visited.add(parentNodes[node])
                    
                    # Push the node on top in the queue
                    queue.append(parentNodes[node])
                    
                # The node on left is the left child
                if node.left and node.left not in visited:
                    
                    # Put the node in the visited set
                    visited.add(node.left)
                    
                    # Push the node on top in the queue
                    queue.append(node.left)
                    
                # The node on right is the right child
                if node.right and node.right not in visited:
                    
                    # Put the node in the visited set
                    visited.add(node.right)
                    
                    # Push the node on top in the queue
                    queue.append(node.right)
                
                # Update the count
                nodesInQueue -= 1
            
            # Update the distance
            k -= 1
            
        # Finally, at this point, the queue will have all the nodes that are at a distance "k" from "targetNode"
        # Construct the output list
        output = []
        while queue: output.append(queue.popleft().val)
            
        # Return the output list
        return output
        

root = TreeNode(3)
target = root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

k = 2

print("Nodes at K distance -> ", Solution().distanceK(root, target,k))
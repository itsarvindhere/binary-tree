from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root):
        
        # To keep track of the root node
        self.root = root
        
        # A Queue to keep the nodes that do not have both left and right child
        # That is, either the node has only left child, or it does not have any child at all
        self.insertionNodes = deque()
        
        # Iterate the tree in BFS and get the nodes for the second last and last level
        queue = deque()
        queue.append(root)
        
        while queue:
            
            # Nodes in current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Push the node in the queue if it does not have a left child
                # Or
                # It has a left child but does not have a right child
                if not node.left or (node.left and not node.right): self.insertionNodes.append(node)
                
                # If the node has a left child, push to the queue
                if node.left: queue.append(node.left)
                
                # If the node has a right child, push to the queue
                if node.right: queue.append(node.right)
                    
                # Update the count
                nodesInCurrentLevel -= 1

    def insert(self, val: int) -> int:
        
        # The new node to insert
        node = TreeNode(val)
        
        # The leftmost node in the queue "self.insertionNodes" will always be the node 
        # that will become the parent of the new node that we have to insert
        parent = self.insertionNodes[0]
        
        # If the parent has a left child already
        if parent.left: 
            
            # The new node will be the right child
            parent.right = node
            
            # Since the parent has both the left and right child, we can safely pop it
            self.insertionNodes.popleft()
        
        # Otherwise, make the new node as the left child
        # And keep the parent node in the queue because it is not yet having a right child
        else: parent.left = node
            
        # Finally, push the new node to the queue as it might become the node to which we have to attach other nodes
        self.insertionNodes.append(node)
        
        # Return the parent node's value
        return parent.val

    def get_root(self):
        
        # Return the root node
        return self.root



root = TreeNode(1)
root.left = TreeNode(2)

obj = CBTInserter(root)
print("Insert 3. Parent is", obj.insert(3))
print("Insert 4. Parent is", obj.insert(4))
print("Root is", obj.get_root())
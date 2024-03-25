from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        # Level Order Traversal output
        output = []
        
        # If there is no node at all
        if not root: return ""
        
        # Queue for Level Order Traversal
        queue = deque()
        queue.append(root)
        
        while queue:
            
            # How many nodes are in current level
            nodesInCurrentLevel = len(queue)
            
            # Go over the nodes in current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in front of the queue
                node = queue.popleft()
                
                # Push the value to the output list
                output.append(str(node.val) if node else "_")
                
                #  Push the left child to the queue
                if node: queue.append(node.left)
                    
                #  Push the right child to the queue
                if node: queue.append(node.right)
                
                # Update the count
                nodesInCurrentLevel -= 1
            
        # Finally, return the output list as string
        return ",".join(output)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # If the "data" string is empty, it means there is no node at all
        if not data: return []
        
        # Convert the data back to a list of values
        data = data.split(",")
        
        # To keep track of the current level
        level = 0
         
        # Queue
        queue = deque()

        # The first value in "data" will always be the value of root node
        # So, create a new root node and also push it to the queue
        root = TreeNode(int(data[0]))
        queue.append(root)
        
        # Pointer to traverse the "data" list
        i = 1
        
        # While the queue is not empty
        while queue:
            
            # Pop the node in front of the queue
            node = queue.popleft()
                
            # The left child
            if data[i] != "_": 
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
                    
            # The right child
            if data[i + 1] != "_": 
                node.right = TreeNode(int(data[i + 1]))
                queue.append(node.right)
                
            # Update "i" by 2 because we already checked left and right child of current node
            i += 2
        
        # Finally, return the tree
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print("Serialized Output -> ", Codec().serialize(root))
print("Deserialized Output -> ", Codec().deserialize(Codec().serialize(root)))
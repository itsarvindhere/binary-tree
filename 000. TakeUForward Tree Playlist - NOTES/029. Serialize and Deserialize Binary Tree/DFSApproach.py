class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    # Pre Order Traversal
    def preOrder(self, root, output):
        
        # If it is a null node
        if not root: 
            output.append("_")
            return
        
        # Put root node's value in the output list
        output.append(str(root.val))
        
        # Traverse left
        self.preOrder(root.left, output)
        
        # Traverse right
        self.preOrder(root.right, output)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        # Pre Order Traversal output
        output = []
        self.preOrder(root, output)
        
        # Finally, return the output list as string
        return ",".join(output)
    
    # Recursive Function to Deserialzie
    def solve(self, data, i):
        
        # If we have a null node
        if data[i[0]] == "_": return None
        
        # The root node for current subtree
        root = TreeNode(int(data[i[0]]))
        
        # Update the index for next node
        i[0] += 1
        
        # Recursive Call for the left subtree
        root.left = self.solve(data, i)
        
        # Update the index for next node
        i[0] += 1
        
        # Recursive Call for the right subtree
        root.right = self.solve(data, i)
        
        # Finally, return the current subtree
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Convert the data back into the list
        data = data.split(",")
        
        # To keep track of the index
        i = [0]
        
        # Recursive function to deserialize
        return self.solve(data, i)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print("Serialized Output -> ", Codec().serialize(root))
print("Deserialized Output -> ", Codec().deserialize(Codec().serialize(root)))
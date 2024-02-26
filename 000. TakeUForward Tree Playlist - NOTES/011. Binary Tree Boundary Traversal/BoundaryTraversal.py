class TreeNode:
    def __init__(self, val):
        self.right = None
        self.val = val
        self.left = None

class Solution:

    # Pre-Order Traversal of a Tree
    def preOrderTraversal(self, root, result):
        
        # Base case
        if not root: return
    
        # Put the value in the result list if this is a leaf node
        if not root.left and not root.right: result.append(root.val)
        
        # Traverse Left
        self.preOrderTraversal(root.left, result)
        
        # Traverse Right
        self.preOrderTraversal(root.right, result)
    
    
    def printBoundaryView(self, root):
        # An array to keep the result of Boundary Traversal
        result = []
        
        # If the root node has a left or right child, put it in the result array
        if root.left or root.right: result.append(root.val)
        
        # First, get the Left Boundary Nodes, except the leaf nodes
        # A leaf node does not have a left or right child
        node = root.left
        while node and (node.left or node.right):
            
            # Put the value in result list
            result.append(node.val)
            
            # Update the node to the left child, if it exists
            # Otherwise, update it to the right child
            node = node.left if node.left else node.right
            
        # Now, we should be at a leaf node by this point
        # So now, we want all the leaf nodes and put their values in the result list
        # To get the left nodes from left to right order, we can use any tree traversal
        # For example, "In order", "Post Order", or "Pre Order"
        # Let's use "Pre-order" for example
        node = root
        self.preOrderTraversal(node, result)
        
        # Finally, we want to get the Right Boundary Nodes, in the reverse order
        # So, we can use a stack for that
        stack = []
        node = root.right
        while node and (node.left or node.right):
            
            # Put the node's value in the stack
            stack.append(node.val)
            
            # Update the node to the right child, if it exists
            # Otherwise, update it to the left child
            node = node.right if node.right else node.left
        
        # Finally, take the nodes in stack and put them in the result list from top to bottom
        while stack: result.append(stack.pop())
        
        # Return the result of the Bounary Traversal
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.right.left = TreeNode(5)
root.left.left.right.right = TreeNode(6)
root.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.right.left.left = TreeNode(10)
root.right.right.left.right = TreeNode(11)

print("Boundary Traversal is -> ", Solution().printBoundaryView(root))
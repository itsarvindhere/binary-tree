# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def binaryTreePaths(self, root):
        
        
        # If there is a single node in the Binary Tree
        if not root.left and not root.right: return [str(root.val)]
        
        # To keep all the paths in the tree
        paths = []
        
        # A Stack
        stack = [root]
        
        # To keep track of the current path
        currentPath = []
        
        # While the stack is not empty
        while stack:
            
            # Take the root on top of the stack
            top = stack.pop()
            
            # Push the node to the current path
            currentPath.append(top)
            
            # If the "top" node is a leaf node
            if not top.left and not top.right:
                
                
                # Push the current path to the list of paths
                path = []
                for node in currentPath: path.append(str(node.val))
                paths.append("->".join(path))
                
                # We will no longer need the node at the end of the current path
                currentPath.pop()
                
                # If the nodes at the end of the "currentPath" is no longer needed
                # How will we check that?
                # If the node we just popped was the "right" node of the node at the end of the currentPath
                # Or, if it is the "left" node and there is no "right" node for the node at the end of currentPath
                # In both cases, we are done with the node at the end of the currentPath
                # Similarly, we can apply the same logic for the node before the node at the end of the currentPath and so on
                # Basically, we are removing all the nodes that are no longer required for the next paths
                node = top
                while currentPath and (currentPath[-1].right == node or (not currentPath[-1].right and currentPath[-1].left == node)):
                    node = currentPath.pop()
                
            # If the root has a right child, push it to the stack
            if top.right: stack.append(top.right)
                
            # If the root has a left child, push it to the stack
            if top.left: stack.append(top.left)
        
        # Return all the paths
        return paths


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right= TreeNode(5)

print("Root to Leaf Paths are -> ", Solution().binaryTreePaths(root))
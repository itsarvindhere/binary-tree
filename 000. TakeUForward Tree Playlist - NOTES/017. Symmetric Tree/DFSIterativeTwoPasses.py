class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        
        # First, we get all the left subtree nodes
        leftSubtreeNodes = []
        
        # Stack
        stack = [root.left]
        
        # While stack is not empty
        while stack:
            
            # Pop the top node
            top = stack.pop()
            
            # Push to the list of left subtree nodes
            leftSubtreeNodes.append(top.val if top else "N")
            
            # If the node is not Null
            if top:
                
                # Push the right child first and then the left child
                stack.append(top.right)
                stack.append(top.left)
        
        # Now, we go over the right subtree nodes
        node = root
        
        # Stack
        stack = [root.right]
        
        # Pointer to iterate over the left subtree nodes from left to right
        i = 0
        
        # While stack is not empty
        while stack:
            
            # Pop the top node
            top = stack.pop()
            
            # Compare to the corresponding node in left subtree
            if (top.val if top else "N") != leftSubtreeNodes[i]: return False
            
            # Update i
            i += 1
            
            # If the node is not Null
            if top:
                
                # Push the left child first and then the right child
                stack.append(top.left)
                stack.append(top.right)
        
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

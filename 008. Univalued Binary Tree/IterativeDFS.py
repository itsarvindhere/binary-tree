class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def isUnivalTree(self, root):
        
        # The value that every node needs to have to make the tree univalued
        val = root.val
        
        # Stack, initially with the root node
        stack = [root]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top
            node = stack.pop()
            
            # If the node does not have same value as "val", the tree is not univalued
            if node.val != val: return False
            
            # Push the right child
            if node.right: stack.append(node.right)
                
            # Push the left child
            if node.left: stack.append(node.left)
            
            
        # The tree is univalued
        return True


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)

print("Output -> ", Solution().isUnivalTree(root))
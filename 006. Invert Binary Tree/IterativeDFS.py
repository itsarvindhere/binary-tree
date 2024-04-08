class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        
        # If there are no nodes
        if not root: return

        # Stack, initially with root node
        stack = [root]
        
        # While the stack is not empty
        while stack:
            
            # Pop the top node
            node = stack.pop()
            
            # Push the right child
            if node.right: stack.append(node.right)
            
            # Push the left child
            if node.left: stack.append(node.left)
                
            # Swap the left and right subtrees
            node.left, node.right = node.right, node.left
        
        # Finally, return the root node
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Output -> ", Solution().invertTree(root))
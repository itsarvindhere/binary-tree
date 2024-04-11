class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to traverse the tree using a stack
    def dfs(self, root, nodeList):
        
        # Stack, initially with root node
        stack = [root]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top
            node = stack.pop()
            
            # If this a leaf node, add it to the list
            if not node.left and not node.right: nodeList.append(node.val)
                
            # Push right child in the stack
            if node.right: stack.append(node.right)
                
            # Push left child in the stack
            if node.left: stack.append(node.left)
    
    def leafSimilar(self, root1, root2):
        
        # Leaf node sequent for root1
        root1Sequence = []
        self.dfs(root1, root1Sequence)
        
        # Leaf node sequent for root2
        root2Sequence = []
        self.dfs(root2, root2Sequence)
        
        # Compare the two
        return root1Sequence == root2Sequence


root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)


root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

print("Output -> ", Solution().leafSimilar(root1, root2))
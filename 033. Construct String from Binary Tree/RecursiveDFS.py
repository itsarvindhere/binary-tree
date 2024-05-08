# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Pre Order Traversal of the Tree (DFS)
    def dfs(self, root, output):
        
        # Base Case
        if not root: return
        
        # Get the root node's value and put it in the output list
        output.append(str(root.val))
        
        # If the root has a left child
        if root.left: 
            
            # Opening Parenthesis
            output.append("(")
            
            # Traverse Left
            self.dfs(root.left, output)
            
            # Closing Parenthesis
            output.append(")")
            
        # If there is no left child but there is a right child, put "()" in the output list
        elif root.right: output.append("()")
            
        if root.right: 
            
            # Opening Parenthesis
            output.append("(")
        
            # Traverse Right
            self.dfs(root.right, output)
        
            # Closing Parenthesis
            output.append(")")
    
    
    def tree2str(self, root):
        
        # A list that we will convert to string when we return it
        output = []
        
        # Call the preorder traversal function
        self.dfs(root, output)
        
        # Return the string
        return "".join(output)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print("Output -> ", Solution().tree2str(root))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        
        # If any one or both trees do not have any nodes
        if not root1 or not root2: return root1 if not root2 else root2
        
        # A stack (Initially with the root nodes of both trees)
        stack = [[root1, root2]]
        
        # While the stack is not empty
        while stack:
            
            # Pop the pair on top of the stack
            node1, node2 = stack.pop()
            
            # Sum the values
            node1.val += node2.val
            
            # If node1 does not have a right child but node2 has it
            # Point the right of "node1" to the right of node2
            if not node1.right and node2.right: node1.right = node2.right
                
            # If both nodes have a right child, push them to the stack
            elif node1.right and node2.right: stack.append([node1.right, node2.right])
                
            # If node1 does not have a left child but node2 has it
            # Point the left of "node1" to the left of node2
            if not node1.left and node2.left: node1.left = node2.left
                
            # If both nodes have a left child, push them to the stack
            elif node1.left and node2.left: stack.append([node1.left, node2.left])
                
        # Return the final tree       
        return root1

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

print("Output -> ", Solution().mergeTrees(root1,root2))
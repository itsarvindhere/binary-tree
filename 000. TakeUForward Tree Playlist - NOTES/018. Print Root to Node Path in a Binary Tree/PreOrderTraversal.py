# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Pre Order Traversal
    def preOrder(self, root, path, val):
        
        # Base case
        # If we reach the leaf node, it means node with value = val is not on this path
        if not root: return False
        
        # Take the root node and put it in the path list
        path.append(root.val)
        
        # If we reached the target node, we return True because we found the path
        if root.val == val: return True
            
        # Traverse left
        isNodeOnLeft = self.preOrder(root.left, path, val)
        
        # If the target node is on the left, we can return True
        # No need to traverse right in that case
        if isNodeOnLeft: return True
        
        # Traverse right
        isNodeOnRight = self.preOrder(root.right, path, val)
        
        # If the target node is on the right, we can return True
        if isNodeOnRight: return True
        
        # If none of the above is valid, it means the target is not on current path
        # Remove the root node from path list and return False
        path.pop()
        return False
    
    def binaryTreePath(self, root, val):
        
        # Path
        path = []
        
        # Path from root to Node with value = val
        self.preOrder(root, path, val)
        
        # Return the path
        return path


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right = TreeNode(3)

val = 7

print("Path is ->", Solution().binaryTreePath(root,val))
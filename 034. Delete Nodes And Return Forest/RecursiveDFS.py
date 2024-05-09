# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        
    # Recursive function to delete the nodes
    def deleteNodes(self, root, parent, isLeftChild, to_delete, rootNodes):
        
        # Base Case
        if not root: return
        
        # If the current node has to be removed
        if root.val in to_delete:
            
            # If parent is not None, let the parent know that this node is deleted
            if parent:
                if isLeftChild: parent.left = None
                else: parent.right = None
                
            # If this node exists in the rootNodes set, remove it
            if root in rootNodes: rootNodes.remove(root)
                
            # Now, the left and right children of this deleted node will be separate trees
            if root.left: rootNodes.add(root.left)
            if root.right: rootNodes.add(root.right)
        
        # If the node doesn't have to be deleted
        # Then, only add it as the root of a tree if it has been detached from its parent
        # That is, if its parent has been deleted already
        # The only exception here is the root node which does not have any parent, hence the "not" check
        elif not parent or parent.val in to_delete: rootNodes.add(root)
            
        # Traverse left
        self.deleteNodes(root.left, root if root.val not in to_delete else None, True, to_delete, rootNodes)
        
        # Traverse right
        self.deleteNodes(root.right, root if root.val not in to_delete else None, False, to_delete, rootNodes)
        
    
    def delNodes(self, root, to_delete):
        
        # Convert the list to a set just to make it easier to lookup
        to_delete = set(to_delete)
        
        # A set to keep all the root nodes of the individual trees that are formed when we delete some node
        rootNodes = set()
        
        # Traverse the tree and delete the required nodes
        self.deleteNodes(root, None, False, to_delete, rootNodes)
        
        # Return the "rootNodes" set as a list
        return list(rootNodes)
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

to_delete = [3,5]

print("Output -> ", Solution().delNodes(root, to_delete))
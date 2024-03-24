# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive Function to build the tree
    def build(self, postorder, inorder, postStart, postEnd, inStart, inEnd, indices):
        
        # Base Case
        # If there are no more nodes, return a Null node
        if postStart > postEnd or inStart > inEnd: return None
        
        # The value at the "postEnd" index in postorder list is the value of the root node of current tree
        root = TreeNode(postorder[postEnd])
        
        # Now, before we recursively call the function for left and right subtrees
        # We need to find how many elements are there in inorder list for the left subtree
        # The inorder for left subtree will be values from inStart to the index of root value in inorder list (excluding itself)
        leftCount = indices[postorder[postEnd]] - inStart
        
        # Now, build the left and right subtrees
        root.left = self.build(postorder, inorder, postStart, postStart + leftCount - 1, inStart, indices[postorder[postEnd]] - 1,indices)
        root.right = self.build(postorder, inorder, postStart + leftCount, postEnd - 1, indices[postorder[postEnd]] + 1, inEnd,indices)
        
        # Return the root node of the tree
        return root
    
    
    def buildTree(self, inorder, postorder):
        
        # Number of nodes
        n = len(inorder)
        
        # A Map to keep track of the indices of node values in "inOrder" list
        indices = {}
        for i in range(n): indices[inorder[i]] = i
            
        # Call the function to build the three which will return the tree after building it
        return self.build(postorder, inorder, 0, n-1, 0, n - 1, indices)


postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]

print("Output -> ", Solution().buildTree(inorder, postorder))
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # Recursive Function to build the tree
    def build(self, preorder, inorder, preStart, preEnd, inStart, inEnd, indices):
        
        # Base Case
        # If there are no more nodes, return a Null node
        if preStart > preEnd or inStart > inEnd: return None
        
        # The value at the "preStart" index in preOrder list is the value of the root node of current tree
        root = TreeNode(preorder[preStart])
        
        # Now, before we recursively call the function for left and right subtrees
        # We need to find how many elements are there in inorder list for the left subtree
        # The inorder for left subtree will be values from index "inStart" to the index of "root" value in inorder (excluding itself)
        leftCount = indices[preorder[preStart]] - inStart
        
        # Now, build the left and right subtrees
        root.left = self.build(preorder, inorder, preStart + 1, preEnd + leftCount, inStart, indices[preorder[preStart]] - 1,indices)
        root.right = self.build(preorder, inorder, preStart + leftCount + 1, preEnd, indices[preorder[preStart]] + 1, inEnd,indices)
        
        # Return the root node of the tree
        return root
        
    
    def buildTree(self, preorder, inorder):
        # Number of nodes
        n = len(inorder)
        
        # A Map to keep track of the indices of node values in "inOrder" list
        indices = {}
        for i in range(n): indices[inorder[i]] = i
            
        # Call the function to build the three which will return the tree after building it
        # Note that we are also passing the start and end indices of both the preorder and inorder lists
        # That's because, when we recursively call this function inside itself,
        # We will pass only a part of preorder and inorder lists in those calls
        # So, we don't want to lose track of the original indices 
        # since our "indices" dictionary only has original indices in it
        return self.build(preorder, inorder, 0, n - 1, 0, n - 1, indices)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print("Output -> ", Solution().buildTree(preorder, inorder))
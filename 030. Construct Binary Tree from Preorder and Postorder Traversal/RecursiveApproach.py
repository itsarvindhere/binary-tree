# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Helper function to construct the tree
    def build(self, preorder, postorder, preStart, preEnd, postStart, postEnd, indices):
        
        # Base Case
        if preStart > preEnd or postStart > postEnd: return None
        
        # The root of the current tree is the value at "preorderStart"
        root = TreeNode(preorder[preStart])
        
        # How many nodes are in the left subtree
        leftCount = 0
        if preStart + 1 <= preEnd: leftCount = indices[preorder[preStart + 1]] - postStart + 1
        
        # Recursively call the function to build the left and right subtrees
        
        # If the left subtree has no nodes, then it simply does not exist
        if leftCount == 0: root.left = None
        else: root.left = self.build(preorder, postorder, preStart + 1, preStart + leftCount, postStart, indices[preorder[preStart + 1]], indices)
            
        root.right = self.build(preorder, postorder, preStart + leftCount + 1, preEnd, postStart + leftCount, postEnd - 1, indices)

        # Return the root of the tree
        return root
    
    
    def constructFromPrePost(self, preorder, postorder):
        # Length of the postorder list
        n = len(postorder)
        
        # A Dictionary that is used to keep track of the indices of values in the postorder list
        indices = {}
        for i in range(n): indices[postorder[i]] = i
            
        # Start and End indices of preorder list
        preStart, preEnd = 0, n - 1
        
        # Start and End indices of postorder list
        postStart, postEnd = 0, n - 1
           
        # Call the helper function that construct the tree and returns its root
        return self.build(preorder, postorder, preStart, preEnd, postStart, postEnd, indices)


preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]

print("Output -> ", Solution().constructFromPrePost(preorder, postorder))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # A Helper function to traverse the tree using Pre-Order traversal
    # And return the result as a list
    def traverse(self, root, output):
        
        # Base Case
        if not root:
            output.append("#")
            return
            
        # Push the node's value in the output list
        output.append(root.val)
            
        # Traverse left
        self.traverse(root.left, output)
        
        # Traverse right
        self.traverse(root.right, output)
    
    
    def isSubtree(self, root, subRoot) -> bool:
        
        # Get the traversals of the two trees
        rootTraversal = []
        subRootTraversal = []
        
        self.traverse(root, rootTraversal)
        self.traverse(subRoot, subRootTraversal)
        
        # Now, we just need to check if "subRootTraversal" is a subarray of "rootTraversal"
        p1, p2 = 0,0
        
        while p1 < len(rootTraversal) and p2 < len(subRootTraversal):
            
            # If the characters are the same, update both pointers
            if rootTraversal[p1] == subRootTraversal[p2]: 
                p1 += 1
                p2 += 1
            
            # Otherwise, reset the two pointers accordingly
            else:
                p1 = p1 - p2 + 1
                p2 = 0
            
            # If we have completely traversed the "subRootTraversal", it means it is a subarray of "rootTraversal"
            # So, we can return True
            if p2 == len(subRootTraversal): return True
        
        # "subRoot" is not a subtree of "root"
        return False


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)


subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print("Output -> ",Solution().isSubtree(root,subRoot))
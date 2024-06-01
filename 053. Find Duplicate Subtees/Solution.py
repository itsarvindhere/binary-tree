# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # A Helper function to traverse the tree using DFS
    def dfs(self, root, rootNodes):
        
        # Base Case
        if not root: return "."
        
        # Traverse left and get the traversal output as string for the left subtree
        leftSubtreeString = self.dfs(root.left, rootNodes)
        
        # Traverse left and get the traversal output as string for the right subtree
        rightSubtreeString = self.dfs(root.right, rootNodes)
        
        # Finally, we can get the traversal output of the tree rooted at "root"
        finalString = "L" + leftSubtreeString + str(root.val) + rightSubtreeString + "R"
        
        # Push to the map
        if finalString in rootNodes:
            rootNodes[finalString][1] += 1
        else:
            rootNodes[finalString]  = [root, 1]
            
        # Return the string for the previous recursive calls
        return finalString
    
    
    def findDuplicateSubtrees(self, root):
        
        # Root Node of Duplicate subtrees
        # The key will be the "string" we get after traversing the tree
        # And value will be a pair [root node, count]
        # Here, count means how many times we got the same "string" after traversing different subtrees
        # All those will be duplicates
        rootNodes = {}
        
        # Traverse the tree to find the duplicate subtrees
        self.dfs(root, rootNodes)
        
        # Finally, just get the root nodes and put them in the output list
        output = []
        for key in rootNodes:
            if rootNodes[key][1] > 1: output.append(rootNodes[key][0])
        
        # Return the required output
        return output

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)

print("Output -> ", Solution().findDuplicateSubtrees(root))
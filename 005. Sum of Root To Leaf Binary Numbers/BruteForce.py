# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    # Helper Function for Recursive DFS
    def dfs(self, root, binary, totalSum):
        
        # Base case
        if not root: return
        
        # Add the current node's value to the binary number so far
        binary.append(str(root.val))
        
        # If this is a leaf node
        if not root.left and not root.right:
            
            # Get the binary number (string) from root to this node
            binaryNumber = "".join(binary)
            
            # Add the binary number to the total (after converting it into decimal)
            totalSum[0] += int(binaryNumber, 2)
            
            # Now, we are done with this leaf node's value and we won't need it again
            # So, we can pop it
            binary.pop()
            
            # And we can return the binary number from here
            return binary
        
        # Make recursive calls for left and right subtrees
        self.dfs(root.left, binary, totalSum)
        self.dfs(root.right, binary, totalSum)
        
        # Once we are done with left and right children, we are also done with the current root node
        # So, we pop its value from the binary number so far
        binary.pop()
    
    def sumRootToLeaf(self, root) -> int:
        
        # To keep track of the binary number from root to leaf
        binary = []
        
        # To get the total sum
        totalSum = [0]
        
        # Call the recursive DFS function
        self.dfs(root, binary, totalSum)
        
        # Return the total sum from root to leaf
        return totalSum[0]


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print("Total Sum -> ", Solution().sumRootToLeaf(root))
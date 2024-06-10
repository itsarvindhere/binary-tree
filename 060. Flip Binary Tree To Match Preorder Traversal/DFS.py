# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Recursive DFS function to find the nodes we have to flip
    def dfs(self, root, voyage, flipped, i):
        
        # If there is no Node
        if not root: return
        
        # If the nodes do not match
        if root.val != voyage[i[0]]: 
            flipped[0] = [-1]
            return
        
        # Update the index
        i[0] += 1
        
        # Check if the next value in voyage is same as the next child (if left child exists otherwise right) 
        
        # If it is not same as left child's value
        if i[0] < len(voyage) and root.left and root.left.val != voyage[i[0]]: 
            # We need to flip the current node
            flipped[0].append(root.val)
            
            # Now, the left child becomes the right child and right child becomes the left child
            # So, we can call the recursive function with the right child first
            # And then with left child
            # So, we are simulating a flip because we do not actually need to flip
            # Since we just want to compare values with "voyage" list
            self.dfs(root.right, voyage, flipped, i)
            self.dfs(root.left, voyage, flipped,i)
            
        # If the next value in voyage list is same as value of left child (or even if left child is not present)
        else:
            
            # No flip is needed at current node
            self.dfs(root.left, voyage, flipped, i)
            self.dfs(root.right, voyage, flipped, i)
            
    
    def flipMatchVoyage(self, root, voyage):
        
        # To keep track of the flipped nodes
        flipped = [[]]
        
        # To iterate over the voyage list
        i = [0]
        
        # Call the recursive DFS function
        self.dfs(root, voyage, flipped, i)
        
        # Return the list
        if not flipped[0]: return []
        
        return flipped[0] if flipped[0][0] != -1 else [-1]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
voyage = [1,3,2]
print("Output -> ", Solution().flipMatchVoyage(root, voyage))
        
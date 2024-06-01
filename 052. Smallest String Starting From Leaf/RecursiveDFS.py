# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to check if a string is lexicographically smaller than the other
    def isSmaller(self, string1, string2):
        
        # If the string2 does not exist
        if not string2: return True
        
        # Lengths
        m,n = len(string1), len(string2)
        
        i = m - 1
        j = 0
        
        while i >= 0 and j < n:
            
            # Compare the characters
            if string1[i] < string2[j]: return True
            elif string1[i] > string2[j]: return False
            else:
                i -= 1
                j += 1
        
        # If string1 is a shorter prefix of string2, return True
        return True if i < 0 else False
    
    # Helper function to iterate the tree in DFS
    def dfs(self, root, currString, smallestString):
        
        # Base Case
        if not root: return
        
        # Add the current character to the "currString"
        currString.append(chr(97 + root.val))
        
        # If this is a leaf node
        if not root.left and not root.right:
            
            # Update the smallest string accordingly
            if self.isSmaller(currString, smallestString[0]): smallestString[0] = "".join(reversed(currString))
        
        # Traverse left
        self.dfs(root.left, currString, smallestString)
        
        # Traverse right
        self.dfs(root.right, currString, smallestString)
        
        # We are done with the current path so we can remove the last character pushed to the list
        currString.pop()
    
    
    def smallestFromLeaf(self, root) -> str:
        
        # To keep track of the smallest string
        smallestString = ['']
        
        # Iterate the tree in DFS and get the smallest string
        self.dfs(root, [], smallestString)
        
        # Return the smallest string
        return smallestString[0]

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

print("Output ->", Solution().smallestFromLeaf(root))
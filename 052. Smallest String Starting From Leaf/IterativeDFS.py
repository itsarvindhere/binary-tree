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
    
    def smallestFromLeaf(self, root) -> str:
        
        # To keep track of the smallest string
        smallestString = ''
        
        # Stack, initially with the root node and the string that we have formed so far
        stack = [[root, []]]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top along with the path so far
            node, currString = stack.pop()
            
            # Put the current node value in the currString formed so far
            currString.append(chr(97 + node.val))
            
            # If this is a leaf node
            if not node.left and not node.right:
                
                # Update the smallest string accordingly
                if self.isSmaller(currString, smallestString): smallestString = "".join(reversed(currString))
            
            # If the node has a right child, push to the stack
            if node.right: stack.append([node.right, currString[:]])
                
            # If the node has a left child, push to the stack
            if node.left: stack.append([node.left, currString[:]])
        
        # Return the smallest string
        return smallestString

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

print("Output ->", Solution().smallestFromLeaf(root))
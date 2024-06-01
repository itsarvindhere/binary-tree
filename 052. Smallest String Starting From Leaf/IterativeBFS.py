from collections import deque


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
        
        # Queue, initially with the root node and the string that we have formed so far
        queue = deque()
        queue.append([root, []])
        
        # While the queue is not empty
        while queue:
            
            # How many nodes are in the current level
            nodesInCurrentLevel = len(queue)
            
            # Iterate over all the nodes in the current level
            while nodesInCurrentLevel > 0:
                
                # Pop the node in the front along with the path so far
                node, currString = queue.popleft()

                # Put the current node value in the currString formed so far
                currString.append(chr(97 + node.val))

                # If this is a leaf node
                if not node.left and not node.right:

                    # Update the smallest string accordingly
                    if self.isSmaller(currString, smallestString): smallestString = "".join(reversed(currString))

                # If the node has a left child, push to the queue
                if node.right: queue.append([node.right, currString[:]])

                # If the node has a right child, push to the queue
                if node.left: queue.append([node.left, currString[:]])
                    
                # Update the count
                nodesInCurrentLevel -= 1
        
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
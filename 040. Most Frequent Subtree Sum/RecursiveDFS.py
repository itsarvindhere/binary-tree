# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # A Helper function to get the sum of the subtrees
    def getSubtreeSum(self, root, subtreeSums):
        
        # Base Case
        if not root: return None
        
        # Sum of left subtree
        leftSubtreeSum = self.getSubtreeSum(root.left, subtreeSums)
        
        # Sum of right subtree
        rightSubtreeSum = self.getSubtreeSum(root.right, subtreeSums)
        
        # If the leftsubtree sum is not None, meaning there is at least one node on the left side
        if leftSubtreeSum != None: subtreeSums[leftSubtreeSum] = subtreeSums.get(leftSubtreeSum, 0) + 1
            
        # If the rightSubtree sum is not None, meaning there is at least one node on the right side
        if rightSubtreeSum != None :  subtreeSums[rightSubtreeSum] = subtreeSums.get(rightSubtreeSum, 0) + 1
            
        if not leftSubtreeSum: leftSubtreeSum = 0
        if not rightSubtreeSum: rightSubtreeSum = 0
        
        # Return the whole subtree sum as a result of previous recursive calls
        return leftSubtreeSum + rightSubtreeSum + root.val
    
    def findFrequentTreeSum(self, root):
        
        # A Dictionary to keep track of the sums and their frequencies
        subtreeSums = {}
        
        treeSum = self.getSubtreeSum(root, subtreeSums)
        subtreeSums[treeSum] = subtreeSums.get(treeSum, 0) + 1
        
        # What is the maximum frequency of a sum
        maxFreq = max(subtreeSums.values())
        
        # Now, we just need to take all the sums with "maxFreq" frequency and put them in the output list
        output = []
        for key in subtreeSums:
            if subtreeSums[key] == maxFreq: output.append(key)
        
        # Finally, return the output list
        return output

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)

print("Output -> ", Solution().findFrequentTreeSum(root))
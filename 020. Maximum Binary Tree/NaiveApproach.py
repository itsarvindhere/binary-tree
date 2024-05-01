from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        
        # Base Case
        if not nums: return
        
        # Iterate over the list and find the maximum element and also the index of maximum element
        maxElement, maxIndex = -inf, -1
        for i in range(len(nums)):
            if nums[i] > maxElement: 
                maxElement = nums[i]
                maxIndex = i
        
        # Root Node (Maximum in the list)
        root = TreeNode(maxElement)
        
        # Make recursive calls for building the left and right subtrees
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])
        
        # Return the final tree
        return root


nums = [3,2,1,6,0,5]

print("Output -> ",Solution().constructMaximumBinaryTree(nums))
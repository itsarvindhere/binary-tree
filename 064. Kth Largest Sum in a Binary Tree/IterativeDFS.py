from heapq import heappush, heappop

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        
    def kthLargestLevelSum(self, root, k: int) -> int:
        
        # A dictionary to keep track of the sum of each level
        levelSums = {}
        
        # A Stack, initially with the root node and its level
        stack = [[root, 1]]
        
        # While the stack is not empty
        while stack:
            
            # Pop the node on top and its level
            node, level = stack.pop()
            
            # Update the dictionary
            levelSums[level] = levelSums.get(level, 0) + node.val
            
            # If there is a right child, push to the stack
            if node.right: stack.append([node.right, level + 1])
                
            # If there is a left child, push to the stack
            if node.left: stack.append([node.left, level + 1])
        
        # Now, get the kth largest level sum
        minHeap = []
        for level in levelSums:
            heappush(minHeap, levelSums[level])
            if len(minHeap) > k: heappop(minHeap)
                
        # Return the kth largest level sum if there are at least "k" levels
        return minHeap[0] if len(minHeap) == k else -1

root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)

k = 2

print("Output -> ", Solution().kthLargestLevelSum(root, k))
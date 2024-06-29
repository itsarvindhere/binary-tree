from heapq import heappush, heappop

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Helper function to traverse the tree in DFS
    def dfs(self, root, level, levelSums):
        
        # Base Case
        if not root: return
        
        # Update the dictionary
        levelSums[level] = levelSums.get(level, 0) + root.val
        
        # Traverse left
        self.dfs(root.left, level + 1, levelSums)
        
        # Traverse right
        self.dfs(root.right, level + 1, levelSums)
        
    def kthLargestLevelSum(self, root, k: int) -> int:
        
        # A dictionary to keep track of the sum of each level
        levelSums = {}
        
        # Call the recursive dfs function to get the level sum
        self.dfs(root, 1, levelSums)
        
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
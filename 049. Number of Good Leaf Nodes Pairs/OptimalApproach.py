# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, count, distance):
        
        # Base Case
        if not root: return []
        
        # If we get a leaf node
        if not root.left and not root.right: return [1]
        
        # Traverse the left subtree and get all the distances of the leaf nodes from current "root"
        leftDistances = self.dfs(root.left, count, distance)
        
        # Traverse the right subtree and get all the distances of the leaf nodes from current "root"
        rightDistances = self.dfs(root.right, count, distance)
        
        # Find how many pairs are there
        for a in leftDistances:
            for b in rightDistances:
                if a + b <= distance: count[0] += 1
        
        # Return the data for the previous root
        data = []
        for val in leftDistances: data.append(val + 1)
        for val in rightDistances: data.append(val + 1)
            
        return data

    def countPairs(self, root, distance: int) -> int:
        
        # To get the count of good leaf node pairs
        count = [0]
        
        # Traverse the tree to get the count
        self.dfs(root, count, distance)
        
        # Return the count of good leaf node pairs
        return count[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

distance = 3

print("Output -> ", Solution().countPairs(root, distance))
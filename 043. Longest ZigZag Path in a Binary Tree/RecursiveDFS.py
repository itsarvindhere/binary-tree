# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # Recursive DFS function
    def dfs(self, root, longestPath, moveLeft, nodesCount):
        
        # Base Case
        if not root: return
        
        # Update the number of nodes in the current path
        nodesCount += 1
        longestPath[0] = max(longestPath[0], nodesCount)
        
        # If we have to move left to stay on the current zig-zag path 
        if moveLeft: 
            
            # Traverse left with the next direction to take as right, hence the flag is False
            self.dfs(root.left, longestPath, False, nodesCount)
            
            # Traverse right with the next direction as left, hence the flag is True
            # But that means we cannot continue with the current path
            # So, a new path will start from the current node towards right, hence the nodesCount is reset to 1 
            # 1, because we want to include current node as starting of the new path)
            self.dfs(root.right, longestPath, True, 1)
            
        # If we have to move right to stay on the current zig-zag path
        else: 
            
            # Traverse right with the next direction to take as left, hence the flag is True
            self.dfs(root.right, longestPath, True, nodesCount)
            
            # Traverse left with the next direction as right, hence the flag is False
            # But that means we cannot continue with the current path
            # So, a new path will start from the current node towards left, hence the nodesCount is reset to 1 
            # 1, because we want to include current node as starting of the new path)
            self.dfs(root.left, longestPath, False, 1)
    
    
    def longestZigZag(self, root):
        
        # The length of the longest path
        longestPath = [0]
        
        # Call the recursive DFS function to get the longest zigzag path
        self.dfs(root, longestPath, False, 0)
        
        # Return the longest path length, that is the number of nodes - 1
        return longestPath[0] - 1

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(1)
root.left.right.left.right = TreeNode(1)

print("Output -> ", Solution().longestZigZag(root))
        
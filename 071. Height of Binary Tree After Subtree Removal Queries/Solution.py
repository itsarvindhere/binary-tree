from heapq import heappop, heappush
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# VIA - https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2757990/Python-3-Explanation-with-pictures-DFS
class Solution:
        
    
    # Traverse the tree and get the level and height data
    def dfs(self, root, currLevel, levels, heights):
        
        # Base Case
        if not root: return 0
        
        # Update the level
        levels[root.val] = currLevel
        
        # Left height
        lHeight = self.dfs(root.left, currLevel + 1, levels, heights)
        
        # Right height
        rHeight = self.dfs(root.right, currLevel + 1, levels, heights)
        
        # Update the height of the subtree rooted at "root"
        heights[root.val] = max(lHeight, rHeight)
        
        return max(lHeight, rHeight) + 1
    
    def treeQueries(self, root, queries):
        
        # Output list to return
        output = []
        
        # For each node, get the informatiom about its level and height of its subtree
        # The level is simply how far the node is from root (Root is at the level 0)
        # The height of a particular node's subtree means how many sublevels the subtree rooted at that node has
        # For example, if we take the first example in the problem, the height of subtree rooted at node "4" is 2
        # Because there are a maximum of two sublevels, one with the node "5" and other with the node "7"
        # The idea is that if we remove any node, then the height of the remaining tree would be the maximum height among the cousins
        # Cousins are simply nodes at the same level as the removed node
        levels, heights = {}, {}
        self.dfs(root, 0, levels, heights)
        
        # Now, for each level, we just want the two maximum height values (from the root to a node)
        maxHeights = defaultdict(list)
        for key in levels:
            heappush(maxHeights[levels[key]], heights[key])
            if len(maxHeights[levels[key]]) > 2: heappop(maxHeights[levels[key]])
                
        # Finally, calculate the final data
        for val in queries:
            
            # Level of the node
            level = levels[val]
            
            # Height of the node
            height = heights[val]
            
            # The two maximum height values of current level
            twoMaxHeights = maxHeights[level]
            
            # If there is only one height value, then it means there is no other node in this level
            # So, the height of the tree when the current node is removed is simply equal to parent's level. That is, level - 1
            if len(twoMaxHeights) == 1: output.append(level - 1)
                
            # If the last entry in the list is the height of node that is being removed
            # Then choose the forst entry
            elif twoMaxHeights[-1] == height: output.append(level + twoMaxHeights[0])
                
            # Otherwise, choose the last entry, which will always be the larger of the two
            else: output.append(level + twoMaxHeights[1])
                
        return output

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(7)

queries = [4]

print("Output -> ", Solution().treeQueries(root, queries))
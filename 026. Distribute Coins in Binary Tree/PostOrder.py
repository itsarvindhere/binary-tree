# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def dfs(self, root, moves):
        
        # Base Case
        if not root: return [0,0]
        
        # Traverse left to get how many nodes are on left and the total sum of values on left
        nodesOnLeft, sumOnLeft = self.dfs(root.left, moves)
        
        # Traverse right to get how many nodes are on right and the total sum of values on right
        nodesOnRight, sumOnRight = self.dfs(root.right, moves)

        # Excess coins on left and right
        leftExcess, rightExcess = sumOnLeft - nodesOnLeft, sumOnRight - nodesOnRight
        
        # Update the moves
        moves[0] += abs(leftExcess) + abs(rightExcess)
        
        # Return the data back for previous recursive calls
        return [nodesOnLeft + 1 + nodesOnRight, sumOnLeft + root.val + sumOnRight]

    def distributeCoins(self, root) -> int:
        
        # Minimum moves
        moves = [0]
        
        # Call the DFS traversal function
        self.dfs(root, moves)
        
        # Return the moves
        return moves[0]


root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)

print("Output -> ", Solution().distributeCoins(root))
        
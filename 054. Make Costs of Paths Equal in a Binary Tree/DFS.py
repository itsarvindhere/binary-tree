class Solution:

    # Recursive DFS function to find the minimum increments
    def dfs(self, i, n, cost, increments):
        
        # Base Case
        if i >= n: return 0
        
        # Get the path cost for the path from current root to any leaf of left subtree 
        # (Since left subtree has same path cost for all the paths)
        leftPathCost = self.dfs((2*i) + 1, n, cost, increments)
        
        # Get the path cost for the path from current root to any leaf of right subtree
        # (Since right subtree has same path cost for all the paths)
        rightPathCost = self.dfs((2*i) + 2, n, cost, increments)
        
        # How many increments are needed to make sure the path cost is same for left and right
        increments[0] += abs(leftPathCost - rightPathCost)
        
        # Return the required value for the previous recursive calls
        return cost[i] + max(leftPathCost, rightPathCost)
    
    
    def minIncrements(self, n: int, cost) -> int:
        
        # Minimum Increments
        increments = [0]
        
        # For the entire tree to follow the property of same path cost
        # Each subtree must follow this property
        self.dfs(0, n, cost, increments)
        
        # Return the minimum increments done
        return increments[0]

n = 7
cost = [1,5,2,2,3,3,1]
print('Output -> ', Solution().minIncrements(n, cost))
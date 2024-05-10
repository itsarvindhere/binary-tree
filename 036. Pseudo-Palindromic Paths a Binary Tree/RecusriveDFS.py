# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # Recursive DFS function
    def dfs(self, root, frequency, count, valuesWithOddFrequency):
        
        # Base Case
        if not root: return
        
        # Update the frequency of the current node's value
        frequency[root.val] = frequency.get(root.val, 0) + 1
        
        # If the frequency becomes odd, put the value in the set
        if frequency[root.val] % 2 != 0: valuesWithOddFrequency.add(root.val)
            
        # If it becomes even, remove it from the set
        else: valuesWithOddFrequency.remove(root.val)
        
        # If this is a leaf node 
        # and
        # If there is at most one element with odd frequency, then this is a pseudo-palindromic path
        if not root.left and not root.right and len(valuesWithOddFrequency) <= 1: count[0] += 1
        
        # Traverse the left subtree
        self.dfs(root.left, frequency, count, valuesWithOddFrequency)
        
        # Traverse the right subtree
        self.dfs(root.right, frequency, count, valuesWithOddFrequency)
        
        # Since we traversed both the left and right subtrees, we won't again visit current "root" node
        # So, reduce the frequency accordingly
        frequency[root.val] -= 1
        
        # If after reducing, its frequency becomes odd, update the set
        if frequency[root.val] % 2 != 0: valuesWithOddFrequency.add(root.val)
        
        # If after reducing, the frequency becomes even, remove it from the set
        else: valuesWithOddFrequency.remove(root.val)
            
    def pseudoPalindromicPaths (self, root):
        
        # To keep track of the count of pseudo palindromic paths
        count = [0]
        
        # A dictionary to keep track of the frequency of values in a path
        frequency = {}
        
        # To keep track of the values that occur odd number of times in current path
        valuesWithOddFrequency = set()
        
        # Call the recursive DFS function to traverse the tree and get the count of paths
        self.dfs(root, frequency, count, valuesWithOddFrequency)
        
        # Return the count
        return count[0]

root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.right = TreeNode(1)
root.right.right = TreeNode(1)

print("Count is -> ", Solution().pseudoPalindromicPaths(root))
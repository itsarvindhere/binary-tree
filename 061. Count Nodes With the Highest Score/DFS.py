from collections import defaultdict
class Solution:
    
    # Recursive DFS function
    def dfs(self, i, parentNodes, nodeCount):
        
        # Base Case  (It is a leaf node)
        if i not in parentNodes: 
            nodeCount[i] = [0,0]
            return 1
        
        leftCount, rightCount = 0,0
        
        if len(parentNodes[i]) > 1:
            
            # Count of nodes in the left subtree
            leftCount = self.dfs(parentNodes[i][0], parentNodes, nodeCount)

            # Count of nodes in the right subtree
            rightCount = self.dfs(parentNodes[i][1], parentNodes, nodeCount)
            
        else:
            
            # Count of nodes in the left subtree
            leftCount = self.dfs(parentNodes[i][0], parentNodes, nodeCount)
            
        
        # Update the dictionary
        nodeCount[i] = [leftCount, rightCount]
        
        # Return the count for the previous recursive calls
        return leftCount + 1 + rightCount
    
    def countHighestScoreNodes(self, parents) -> int:
        
        # Total Number of nodes
        n = len(parents)
        
        # A dictionary to keep track of the parent and the children of that parent node
        parentNodes = defaultdict(list)
        for i in range(n): parentNodes[parents[i]].append(i)
        
        # First, for each node, we need to find the count of nodes in each of the subtrees rooted at children nodes
        # A dictionary where key will be the node value and value will be a pair [leftCount, rightCount]
        nodeCount = {}
        
        # Call the recursive DFS function to count the nodes
        self.dfs(0, parentNodes, nodeCount)
        
        # Now, we have to find the highest score and the number of nodes with that highest score
        highestScore = 0
        count = 0
        
        # For each node
        for i in range(n):
            
            # What if this node is removed along with its edges?
            # We now have to find product of sizes of all the subtrees that are left
            # If current node is removed, we will get at most three different subtrees
            # One that is on the top of the node that we just removed
            # One will be the subtree rooted at the left child of the current node
            # One will be the subtree rooted at the right child of the current node
            
            # First, we check for the topCount
            # If we know how many nodes the left and right subtrees have
            # We can say the tree on top will have nodes = totalNodes - (leftCount + 1 + rightCount)
            topCount = n - (nodeCount[i][0] + 1 + nodeCount[i][1])
            
            # Now, we check for left and right children
            leftCount, rightCount = nodeCount[i][0], nodeCount[i][1]
            
            # To avoid issues due to multiplication with 0
            if leftCount == 0: leftCount = 1
            if rightCount == 0: rightCount = 1
            if topCount == 0: topCount = 1
                
            # What is the score of the node
            score = leftCount * rightCount * topCount
            
            # Check if the current score is greater than the highest score so far
            if score > highestScore:
                
                # Update the highest score
                highestScore = score
                
                # Rest the count
                count = 1
                
            # If it is equal to the highest score, update the node count
            elif score == highestScore: count += 1
        
        # Return the count of nodes with the highest score
        return count


parents = [-1,2,0,2,0]
print("Output -> ", Solution().countHighestScoreNodes(parents))
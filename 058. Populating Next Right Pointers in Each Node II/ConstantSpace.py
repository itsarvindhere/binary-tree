# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:

    # Helper function to find the next node in current level that has at least one child
    def findNext(self, root):
        temp = root.next
        while temp and not temp.left and not temp.right: temp = temp.next
            
        return temp
    
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # Temporary variable to not lose track of the root node
        ogRoot = root
        
        # In the beginning of each iteration, "root" will be always be the first node of current level
        while root:
            
            # Now, we will go over the nodes in current level from left to right
            temp = root
            while temp:
                
                # Update the next right pointer for the left child
                if temp.left:
                    if temp.right: temp.left.next = temp.right
                    else: 
                        newTemp = self.findNext(temp)
                        if newTemp: temp.left.next = newTemp.left if newTemp.left else newTemp.right
                        
                # Update the next right pointer for the right child
                if temp.right:
                    newTemp = self.findNext(temp)
                    if newTemp: temp.right.next = newTemp.left if newTemp.left else newTemp.right
                
                # Update "temp"
                temp = temp.next
                
            # Update "root" accordingly
            
            # If there is at least one child, update root to that child
            if root.left or root.right: root = root.left if root.left else root.right
                
            # Otherwise, we need to update it to the leftmost node of next level, if it exists
            else:
                newTemp = self.findNext(root)
                if newTemp: root = newTemp.left if newTemp.left else newTemp.right
                else: break
                
                
        # Return the original root node after updating the next pointers accordingly
        return ogRoot

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

print("Output -> ", Solution().connect(root))
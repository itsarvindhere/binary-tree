from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        
        # If the tree is empty
        if not root: return root
        
        # Traverse each level
        tempRoot = root
        while tempRoot.left:
            
            temp = tempRoot
            while temp:
                
                # 'temp.left' is the first node of the next level
                # So, its next pointer (temp.left.next) will point to "temp.right"
                temp.left.next = temp.right

                # Similarly, for "temp.right", its next pointer will point to 'temp.next.left'
                if temp.next: temp.right.next = temp.next.left

                # Update the temp
                temp = temp.next
                
            # Update tempRoot
            tempRoot = tempRoot.left
            
        # Finally, return the tree
        return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Output -> ", Solution().connect(root))
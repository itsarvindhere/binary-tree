It does not matter if you use C++, Java, Python or any other language to learn DSA. The basic idea will be the same for all when it comes to representing a Binary Tree in the code.

In Python, we create a Tree data structure using the concept of nodes.

We create a class, normally called "Node", which has three properties -> left, right, and data (or "val", whatever you want to name it).

"left" and "right" are also objects of type "Node" and "data" is the actual value in the current node.

So for example, let's consider a simple Binary Tree which has a root node with value "10", there is a left node with value "2" and a right node with value "4"

So, this is how we will write the same in code - 

First, we define a "Node" class - 

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

And now, we create our root node as - 

    root = Node(10)

Now, we define its left and right children - 

    root.left = Node(2)
    root.right = Node(4)

So, the left child is a Node with a value "2" and the right child is a node with value "4".

And in this way, we represent Binary Trees in Python.


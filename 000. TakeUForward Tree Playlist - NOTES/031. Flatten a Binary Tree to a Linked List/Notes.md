# PROBLEM STATEMENT

Given the root of a binary tree, flatten the tree into a "linked list":

 - The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
 - The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# EXAMPLE

![alt text](image.png)

# APPROACH

The thing that makes this problem complex is the fact that we have to change the structure of the original tree instead of creating a new linked list itself. In other words, we have to convert the Tree into a Linked List "In-Place".

Otherwise, it should've been a pretty straightforward problem.

## APPROACH #1 - NOT EFFICIENT

The first approach is not that efficient. But, basically, what we will do is, we will first flatten out the left subtree, and then the right subtree, and then, we have to attach them accordingly.

![alt text](image.png)

Let's say we have the above test case.

So, when we are at the root node 1, we will make two calls. One to flatten the left subtree and one to flatten the right subtree. Our recursive function is going to work in such a way that whatever tree we give it, it will flatten it out and return its root back.

So, at the end of both the calls, we should have a flatten left subtree as 2 -> 3 -> 4 and a flatten right subtree as 5 -> 6

And now, its time to join them with the root node correctly.

As the problem statement says, we have to make left child of root as Null, then we need to attach the portion "2 -> 3 -> 4" to the root, and then we need to attach the portion "5 -> 6" to the end of "2 -> 3 -> 4".

And eventually, we get "1 -> 2 -> 3 -> 4 -> 5 -> 6"

Now, the problem here is that when we get a flat left subtree, we do not know what is the last node in that tree. And this is important because we can only attach the flat right subtree to the end of a flat left subtree, if we know the last node. Because to this last node, we have to attach the flat right subtree.

And so, for that, we have to again traverse the left subtree just to reach this last node, and this means, we are doing an extra traversal inside a traversal. And that's not efficient. Yes, this will pass all the test cases but still, we can do better.

## APPROACH #2 - EFFICIENT

So, the idea remains almost the same as before. The change is that, when we return some value from our recursive function, we will always return the last node in the current tree. 

What is the last node? Last node means the rightmost node in the last level of a tree. 

![alt text](image.png)

For example, if we have the above tree, when we are at the node 3, the last node is itself. Because there are no left or right children. 

When we are at the node "2", the last node in left subtree is "3" whereas the last node in right subtree is "4". But, when we return a value, we have to return the last node in this subtree that has root = 2. That will be the node "4". If the node "4" was not there, then it would've been the node "3". But in above example, node "4" is the last node in last level hence it will be returned.

And so, when we are at the node "1", we will get the last node in left subtree as "4".  

And this small change will eliminate the need to traverse the left subtree again, just to find the last node.
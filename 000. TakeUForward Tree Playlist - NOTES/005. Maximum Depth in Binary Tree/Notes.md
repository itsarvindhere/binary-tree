# PROBLEM STATEMENT

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# EXAMPLE

![Alt text](image.png)

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

# APPROACH #1 - RECURSION

We have two different ways to deal with this problem. Either we can use the Recursive approach or we can use the Level Order Traversal (using a Queue).

![Alt text](image.png)

So, let's take the tree above.

If we are at the node {3}, and we have to find the number of nodes from this root node to the farthest leaf node, we can say that the maximum depth will be - 

    1 + max(max depth of left subtree, max depth of right subtree)

Here we add "1" because we are already at root node so we have to count that as well.

So for above example, when we are at node {3}, the max depth of left subtree is 1 and the max depth of right subtree is 2. So, the maximum depth becomes - 

     1 + max(1,2) => 1 + 2 => 3

Hence, the output is "3" for the above example.

And that's the whole idea.

We will recursively traverse the tree, first on left side and then on right side.

And finally, we will get the maximum depth of the tree.

# APPROACH #2 - LEVEL ORDER TRAVERSAL

We can also use Level Order Traversal to find the maximum depth of a Binary Tree. Because, as we know, in Level Order Traversal, we go over nodes in each level. And if you think of it, the total number of levels = maximum depth of a tree, isn't it?

And that's the whole idea. Just do a Level Order Traversal of the tree and at the end, return the total number of levels in the tree. That would be the maximum depth.

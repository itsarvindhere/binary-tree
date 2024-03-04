# PROBLEM STATEMENT

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# EXAMPLE

![alt text](image.png)

Output: true

# BFS APPROACH - ITERATIVE

We can use Level Order Traversal to solve this problem. Looking at the above example, we can see that except the root node, we are simply comparing the nodes in each level in this way -

    In level 1, we have two nodes [2, 2]

    And if we divide this list from center, we get node 2 on left and node 2 on right. Since values in each half are mirror images of each other, it means the tree is symmetric so far

    In level 2, we have four nodes [3,4,4,3]

    Again, if we divide from center, we get [3,4] on one side and [4,3] on other. Since these are mirror images of each other, the tree is symmetric.

Let's take another example that includes "Null" nodes as well.

![alt text](image-1.png)

    For above image, in level 1, we have [2,2]
    So, tree is symmetric so far

    Now, in level 2, we have [Null, 3, Null, 3]

    If we divide it from center we get [Null ,3] and [Null ,3]

    But, ideally it should've been [Null,3] and [3, Null]

    So, the tree is not symmetric

So, that's how we will compare the nodes in a level in the BFS Approach. We will first go over all nodes in the level till the center point and then, for next nodes, we will compare them with the nodes on left side, one by one. If at any place they mismatch, then we know tree is not symmetric.


# DFS APPROACH - ITERATIVE - TWO PASSES

We can use DFS as well. As we know, for DFS, we use a Stack in the iterative approach.

We can first go over all the nodes in the root.left subtree. 

And then, we go over all the nodes in root.right subtree and keep comparing them to the left subtrees nodes. If at any place they mismatch, we know the tree is not symmetric.

The code is a bit lengthy because we have to while loops one after the other. But, we can do all this in a single while loop as well.

# DFS APPROACH - ITERATIVE - ONE PASS

We know that for any two nodes "A" and "B" on left and right side of the center line, this is how their children node values must be matched - 

    A.left = B.right
    A.right = B.left

So, we can use a stack to always have the top two nodes as the mirror nodes. 

So, stack will be like this from top to bottom at any time [B.right, A.left, B.left, A.right..... so on]

And so, at any time, we can pop the top two nodes which we know should have same values because they are the mirror nodes.  If they don't have same values we know the tree is not symmetrical.

# DFS APPROACH - RECURSIVE

The recursive solution is pretty simple and short. 

All we want to make sure is that two mirror nodes have same values and their corresponding mirror children are also same.

So, we can have a recursive function, lets call it "isMirror", that takes the mirror nodes "left" and "right". And then it just checks if - 

    left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
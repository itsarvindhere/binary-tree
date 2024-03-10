# PROBLEM STATEMENT

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# EXAMPLE

![alt text](image.png)

Input: p = 5, q = 4
Output: 5

Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# NAIVE APPROACH

# **1. NAIVE APPROACH - TWO TRAVERSALS**
In the Naive approach, we first get the path from Root to Node "p" and then we get the path from Root to Node "q".

And then, we traverse over both the paths till we find the rightmost node in both the paths that is same for both nodes.

That rightmost node will be the Lowest Common Ancestor.

![alt text](image.png)

For example, if we have the above Binary Tree and p and q are the Nodes {7} and {4} respectively, this is what we will do -

	Path from Root to Node {7} => [3,5,2,7]
	Path from Root to Node {4} => [3,5,2,4]
	
	Now, if we compare the two paths - 
	
	First, we get "3" at index = 0 in both paths so we update lca = {3}
	Next, we get "5" at index = 1 in both paths so we update lca = {5}
	And then, we get "2" at index = 2 in both paths so we update lca = {2}
	At index = 3, the nodes are different so we stop.
	
	Hence, the lca is {2}
	
The issue is that we have to traverse the Tree Twice, once to find the path from Root to "p" and then to find the path from Root to "q". But, there is a better way to solve this problem.

# **2. OPTIMAL APPROACH - ONE TRAVERSAL**

![alt text](image.png)

Let's take the same example as before. Nodes p and q are {7} and {4}, respectively.

Basically, our Recursive DFS function will give us one of two values - 

	1. Either it gives us a "None" which means the current "root" node is not the ancestor of "p" or "q"
	2. Or, it gives us some node which will be the Ancestor of the nodes "p" and "q"

So, let's start with the root node {3}. Is this node p or q? No. So the first if check fails and we continue.

Now, we traverse the left side of {3} by making a recursive call to the left subtree.

-------------------------------------------------------------------

The call made is preOrder(5, 7, 4) which means root node is "5", p is "7" and q is "4"

Now, we are at the node {5}. We check if 5 is one of the nodes p or q. It is not. So, if check fails and we continue.

Now again, we will make a recursive call for the left traversal.

-------------------------------------------------------------------

The call made is preOrder(6,7,4) which means root node is "6", p is "7" and q is "4"

We check if 6 is one of the nodes p or q. It is not. So, if check fails and we continue.

Now again, we will make a recursive call for the left traversal.

-------------------------------------------------------------------

The call made is preOrder(None,7,4) which means root node is "None", p is "7" and q is "4"

We check if 6 is one of the nodes p or q. It is not. But, the root is "None" which means we cannot go left anymore. So, we will return the root node at this point which is "None". So, "None" is returned from this call.

-------------------------------------------------------------------

Now, we come back to the function preOrder(6,7,4) and we are done with left traversal so we make a call for right traversal and the same thing happens.

Hence, for the function preOrder(6,7,4) both the left and right traversals give us "None" and so we return None.

-------------------------------------------------------------------

We now come back to the function preOrder(5,7,4) and we are done with the left traversal. Now, we do the right traversal. So, we make a call preOrder(2,7,4).

The call made is preOrder(2,7,4) which means root node is "2", p is "7" and q is "4"

We check if 2 is one of the nodes p or q. It is not. It is not so if check fails.

Now, we do a left traversal first by calling preOrder(7,7,4).

-------------------------------------------------------------------
The call made is preOrder(7,7,4) which means root node is "7", p is "7" and q is "4"

We check if 7 is one of the nodes p or q. YES IT IS! So, it means node {7} is an ancestor of one of the nodes p and q. Remember that a node can be the descendant of itself. And so, we return the node {7} and there is no need to do left or right traversal at this point.

So, from preOrder(7,7,4), we return {7}. We come back to the function preOrder(2,7,4) and we do the right traversal. So, wecall preOrder(4,7,4)

-------------------------------------------------------------------
The call made is preOrder(4,7,4) which means root node is "4", p is "7" and q is "4"

We check if 4 is one of the nodes p or q. YES IT IS! So, it means node {4} is an ancestor of one of the nodes p and q.  And so, we return the node {4} and there is no need to do left or right traversal at this point.

-------------------------------------------------------------------

So now, in the function preOrder(2,7,4), the left traversal gave us node {7} and the right traversal gave us the node {4}. What does it mean? It means that the node {2} is the common ancestor of both the nodes. So, from preOrder(2,7,4), we return {2}. Remember that we either return "None" or we return the ancestor.

So, we come back to preOrder(5,7,4) and its left traversal gave None and right traversal gave {2}. So, we return the non Null value which is {2}.

Now, we come back to preOrder(3,7,4) and we are done with left traversal which gave us {2}

We will do right traversal which will give us None.

So, when we are at the root node {3}, left traversal gave us the node {2} and the right traversal gave us the node None. And since we always return the Non Null value is both are not Null, we will return {2}.

And so, {2} is the LOWEST COMMON ANCESTOR.

This is how the Optimal Recursive Approach works.
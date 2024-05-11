*** To make it easier for students to understand, I have written this code as simple as possible

# knapsack-lower-upper-bound
The knapsack problem deals with maximizing the value you can get from items that fit within a weight limit. Lower and upper bounds help us efficiently search for the optimal solution in certain knapsack algorithms like branch and bound.

## Lower Bound:
This represents the guaranteed minimum value you can achieve considering the items already included and some strategy for the remaining ones. It helps prune out branches in the search tree that can never lead to a better solution than the current lower bound.

## Upper Bound:
This is an estimate of the maximum value you might get. It's not guaranteed to be achievable, but it serves as a reference point. If the upper bound for a particular branch in the search tree is lower than the current best solution (tracked by the lower bound), we can safely ignore that branch because it cannot possibly lead to a better outcome.

There are different techniques to calculate these bounds, and they influence how effectively the algorithm explores the search space. The key idea is to use these bounds to strategically focus on promising parts of the search tree and avoid exploring branches that cannot lead to the optimal solution.

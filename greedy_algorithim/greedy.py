# Python Program to find the minimum number of coins
# to construct a given amount using greedy approach

"""
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems. 

An optimization problem can be solved using Greedy if the problem has the following property: 

At every step, we can make a choice that looks best at the moment, and we get the optimal solution to the complete problem. 
Some popular Greedy Algorithms are Fractional Knapsack, Dijkstra’s algorithm, Kruskal’s algorithm, Huffman coding and Prim’s Algorithm 

Problem structure:
Most of the problems where greedy algorithms work follow these two properties:
1). Greedy Choice Property:- This property states that choosing the best possible option at each step will lead to the best overall solution. If this is not true, a greedy approach may not work.
2). Optimal Substructure:- This means that you can break the problem down into smaller parts, and solving these smaller parts by making greedy choices helps solve the overall problem

How to Identify Greedy Problems:
There are two major ways to detect greedy problems -
1). Can we break the problem into smaller parts? If so, and solving those parts helps us solve the main problem, it probably would be solved using greedy approach. For example - In activity selection problem, once we have selected a activity then remaining subproblem is to choose those activities that start after the selected activity.
2). Will choosing the best option at each step lead to the best overall solution? If yes, then a greedy algorithm could be a good choice. For example - In Dijkstra’s shortest path algorithm, choosing the minimum-cost edge at each step guarantees the shortest path.


Difference between Greedy and Dynamic Programming:
1). Greedy algorithm works when the problem has Greedy Choice Property and Optimal Substructure, Dynamic programming also works when a problem has optimal substructure but it also requires Overlapping Subproblems.
2). In greedy algorithm each local decision leads to an optimal solution for the entire problem whereas in dynamic programming solution to the main problem depends on the overlapping subproblems.

"""
def minCoins(coins, amount):
    n = len(coins)
    coins.sort()
    res = 0

    # Start from the coin with highest denomination
    for i in range(n - 1, -1, -1):
        if amount >= coins[i]:
            
            # Find the maximum number of ith coin we can use
            cnt = amount // coins[i]

            # Add the count to result
            res += cnt

            # Subtract the corresponding amount from the total amount
            amount -= cnt * coins[i]

        # Break if there is no amount left
        if amount == 0:
            break
    return res

if __name__ == "__main__":
    coins = [5, 2, 10, 1]
    amount = 39

    print(minCoins(coins, amount))
    
    
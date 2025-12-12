"""
Given an array arr[] of non-negative integers and a value sum, the task is to check if there is a subset of the given array whose sum is equal to the given sum. 

Examples:
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output: False
Explanation: There is no subset that add up to 30.

Follow the below steps to implement the recursion:
Build a recursive function and pass the index to be considered (here gradually moving from the last end) and the remaining sum amount.
For each index check the base cases.
If the answer is true for any recursion call, then there exists such a subset. Otherwise, no such subset exists.
"""
# Using Recursion – O(2^n) Time and O(n) Space
# problem using recursion
def isSubsetSumRec(arr, n, sum):
  
    # Base Cases
    if sum == 0:
        return True
    if n == 0:
        return False

    # If the last element is greater
    # than the sum, ignore it
    if arr[n - 1] > sum:
        return isSubsetSumRec(arr, n - 1, sum)

    # Check if sum can be obtained by including
    # or excluding the last element
    return (isSubsetSumRec(arr, n - 1, sum) or 
            isSubsetSumRec(arr, n - 1, sum - arr[n - 1]))
    
arr = [3, 34, 4, 12, 5, 2]
sum = 9
print(isSubsetSumRec(arr,len(arr),sum))
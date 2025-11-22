"""
🔹 Linear Search

Definition: Check each element in the list one by one until the target is found or the list ends.
Works On: Both sorted and unsorted lists.
Approach: Sequential search.
Time Complexity:
Best Case: O(1) (if target is at the beginning)
Worst Case: O(n) (if target is at the end or not present)
Space Complexity: O(1) (no extra memory needed).
Ease of Use: Simple, easy to implement.
Efficiency: Slow for large datasets.
"""

def linear_search(arr,target):
    for i in range(len(arr)-1):
        if arr[i]==target:
            return i
    return -1
arr=[12,45,3,27,8,19,0]
target=19
x=linear_search(arr,target)
if x!=-1:
    print(f"element found at index {x}")
else:
    print("elment not found")
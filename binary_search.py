"""
Binary Search

Definition: Repeatedly divides the sorted list into halves to locate the target.
Works On: Only sorted lists/arrays.
Approach: Divide and Conquer.
Time Complexity:
Best Case: O(1) (if middle element is the target)
Worst Case: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive implementation.
Ease of Use: Slightly more complex to implement than linear search.
Efficiency: Much faster than linear search on large datasets.
"""
def bineary_search(arr,target):
    left, right= 0, len(arr)-1
    while left<=right:
        mid=(left+right)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
            
    return -1

arr=[12,4,6,22,76,14]
target=4
x=bineary_search(arr, target)
if x!=-1:
    print(f"element found at index {x}")
else:
    print("element not found")
    
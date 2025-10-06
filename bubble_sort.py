"""
Bubble Sort:
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top.

How it Works:
Compare adjacent elements
If they are in wrong order, swap them
Continue for all pairs in the array
Repeat the process until no swaps are needed

Time Complexity
Best Case: O(n) - When array is already sorted (with optimized version)
Average Case: O(n²) - On average, we need to do n²/2 comparisons
Worst Case: O(n²) - When array is sorted in reverse order

Space Complexity
O(1) - Only uses a constant amount of extra space
"""

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                
    return arr
arr=[64,25,12,22,11]
x=bubble_sort(arr)
print(x)

"""
def bubble_sort(arr):
    '''
    Sorts an array using bubble sort algorithm
    
    Args:
        arr: List of comparable elements to be sorted
    
    Returns:
        None (sorts in-place)
    '''
    n = len(arr)  # Get the length of array
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        # So we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
"""
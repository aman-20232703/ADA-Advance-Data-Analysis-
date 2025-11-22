"""
1.Selection Sort:
Selection Sort is a simple comparison-based sorting algorithm that divides the input list into two parts: a sorted portion at the beginning and an unsorted portion at the end. It repeatedly selects the smallest (or largest) element from the unsorted portion and moves it to the sorted portion.

How it Works:
Find the minimum element in the unsorted portion
Swap it with the first element of the unsorted portion
Move the boundary of sorted and unsorted portions one element to the right
Repeat until the entire array is sorted

Time Complexity
Best Case: O(n²) - Even if array is already sorted, we still need to check all elements
Average Case: O(n²) - On average, we perform n²/2 comparisons
Worst Case: O(n²) - When array is sorted in reverse order

Space Complexity
O(1) - Only uses a constant amount of extra space
"""

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        mid=i
        for j in range(i+1, n):
            if arr[mid]>arr[j]:
                mid=j
        arr[i],arr[mid]=arr[mid],arr[i]
    return arr
arr=[64,25,12,22,11]
x=selection_sort(arr)
print(x)

"""
def selection_sort(arr):

    '''
    Sorts an array using selection sort algorithm
    
    Args:
        arr: List of comparable elements to be sorted
    
    Returns:
        None (sorts in-place)
    '''
    n = len(arr)  # Get the length of array
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i  # Assume current element is minimum
        
        # Check all elements after position i
        for j in range(i + 1, n):
            # If we find a smaller element, update min_idx
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        # of unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
"""
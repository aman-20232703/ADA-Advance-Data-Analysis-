"""
Definition
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time by repeatedly inserting a new element into the sorted portion of an array. It works similar to how you sort playing cards in your hands.

How it Works
Start with the second element (consider first element as sorted)
Compare it with elements in the sorted portion
Shift elements greater than current element to the right
Insert current element at its correct position
Repeat for all elements

Time Complexity
Best Case: O(n) - When array is already sorted (only one comparison per element)
Average Case: O(n²) - On average, each element is compared with half the sorted portion
Worst Case: O(n²) - When array is sorted in reverse order

Space Complexity
O(1) - Only uses a constant amount of extra space
"""
def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            
        arr[j+1]=key
    return arr
arr=[64,25,12,22,11]
x=insertion_sort(arr)
print(x)
        
        
"""
def insertion_sort(arr):
    '''
    Sorts an array using insertion sort algorithm
    
    Args:
        arr: List of comparable elements to be sorted
    
    Returns:
        None (sorts in-place)
    '''
    n = len(arr)  # Get the length of array
    
    # Traverse through 1 to n (start from second element)
    for i in range(1, n):
        # Store the current element to be inserted
        key = arr[i]
        
        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead of their current position
        j = i - 1  # Start from the last element of sorted portion
        
        # Keep moving elements right while they are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1  # Move to previous element
        
        # Place key at its correct position
        arr[j + 1] = key
    
    return arr
"""


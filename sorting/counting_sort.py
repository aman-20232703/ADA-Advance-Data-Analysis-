"""
Counting Sort is a non-comparison-based sorting algorithm that sorts integers by counting the frequency of each distinct element in the input. It works well when the range of input values is not significantly larger than the number of elements to be sorted.

How it Works (Steps)

Find the range (k):
Identify the maximum element in the input array.

Initialize count array:
Create a count array of size k+1 initialized to 0.

Count frequencies:
Traverse the input array and increase the count for each element.

Compute cumulative count:
Modify the count array such that each element at index i stores the total number of elements ≤ i.

Build output array:
Place each input element in its correct sorted position using the cumulative count, traversing input in reverse to maintain stability.

Copy result:
Copy the sorted output back into the original array if required.

case	Time Complexity	Reason
Best Case	O(n + k)	Always counts and places elements
Average Case	O(n + k)	Same process for all inputs
Worst Case	O(n + k)	No extra comparisons needed
"""



def counting_sort(arr):
    max_v=max(arr)
    count=[0]*(max_v+1)
    
    for num in arr:
        count[num]+=1
    
    for i in range(1, len(arr)):
        count[i]+=count[i-1]
        
    output=[0]*len(arr)
    for num in reversed(arr):
        output[count[num]-1]=num
        count[num]-=1
        
    return arr

arr=[4,6,3,4,2,3,1]
x=counting_sort(arr)
print(x)


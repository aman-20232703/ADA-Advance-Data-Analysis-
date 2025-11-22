"""
Heap sort is a comparison-based sorting technique based on Binary Heap Data Structure.it can be implemented either a min heap or max heap but its comonly implemented using a max heapntp sort in asc. order

steps of heap sort:
First convert the array into a max heap using heapify,
Then one by one delete the root node of the Max-heap and replace it with the last node and heapify. 
Repeat this process while size of heap is greater than 1.
Finally we get sorted array.

Time Complexity
Case	Time Complexity	Explanation
Best	O(n log n)	Building heap + heapifying each node
Average	O(n log n)	Each extraction costs log n
Worst	O(n log n)	Same as above
"""

def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    
    if left<n and arr[left]>arr[largest]:
        largest=left
        
    if right<n and arr[right]>arr[largest]:
        largest=right
        
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n=len(arr)
    
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
        
    return arr

arr=[64,25,11,22,12]
x=heap_sort(arr)
print(x)
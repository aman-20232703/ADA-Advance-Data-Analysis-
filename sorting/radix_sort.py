"""
Radix Sort is a linear (for fixed length digit counts) or no-comperison based sorting algorithim that sorts elements by processing them digit by digit. It is an efficient sorting algorithm for integers or strings with fixed-size keys. 

It repeatedly distributes the elements into buckets based on each digit's value. This is different from other algorithms like Merge Sort or Quick Sort where we compare elements directly.
By repeatedly sorting the elements by their significant digits, from the least significant to the most significant, it achieves the final sorted order.
We use a stable algorithm like Counting Sort to sort the individual digits so that the overall algorithm remains stable.

Time Complexity:
~ Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping the keys by the individual digits which share the same significant position and value. It has a time complexity of O(d * (n + b)), where d is the number of digits, n is the number of elements, and b is the base of the number system being used.
~ In practical implementations, radix sort is often faster than other comparison-based sorting algorithms, such as quicksort or merge sort, for large datasets, especially when the keys have many digits. However, its time complexity grows linearly with the number of digits, and so it is not as efficient for small datasets.
"""


def counting_sort(arr,exp):
    n=len(arr)
    output=[0]*n
    count=[0]*10
    
    for i in range(n):
        index=(arr[i]//exp)%10
        count[index]+=1
        
    for i in range(1,10):
        count[i]+=count[i-1]
        
    i=n-1
    while i>=0:
        index=(arr[i]//exp)%10
        output[count[index]-1]=arr[i]
        count[index]-=1
        i-=1
        
    for i in range(n):
        arr[i]=output[i]

def radix_sort(arr):
    max_v=max(arr)
    exp=1
    while max_v//exp>0:
        counting_sort(arr,exp)
        exp*=10
    return arr
arr=[64,25,12,22,11]
x=radix_sort(arr)
print(x)



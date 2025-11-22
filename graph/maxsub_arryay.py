def maxSubarray(arr):
    max_sum = float('-inf')
    sum = 0
    start = end = temp_start = 0

    for i,num in enumerate(arr):
        if sum <= 0:
            sum = num
            temp_start = i
        else:
            sum += num

        if sum > max_sum:
            max_sum = sum
            start = temp_start
            end = i

    return max_sum,arr[start:end+1]

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = maxSubarray(arr)
print("Maximum subarray sum:", max_sum)
print("Subarray:", subarray)
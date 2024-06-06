# Input: arr = {-2,-3,4,-1,-2,1,5,-3}
# Output: 7
# Explanation: The subarray {4,-1, -2, 1, 5} has the largest sum 7.
# Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 
# Kadane’s algorithm
# The subarray with negative sum is discarded (by assigning max_so_far = 0 in code).
# We carry subarray till it gives positive sum.

def maxSubArraySum(array, size):

    max_sum_so_far = 0
    curr_sum = 0
    for i in range(0, size):
        curr_sum = curr_sum + array[i]
        if max_sum_so_far < curr_sum:
            max_sum_so_far = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]

print(maxSubArraySum(a, len(a)))

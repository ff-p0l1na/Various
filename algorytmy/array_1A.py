# To print the subarray with the maximum sum the idea is to maintain start 
# index of curr_sum at current index so that whenever 
# maximum_sum_so_far is updated with curr_sum then start index
#  and end index of subarray can be updated with start and current index.

from sys import maxsize

def maxSubArraySum(a, size):

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))


# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a, len(a))
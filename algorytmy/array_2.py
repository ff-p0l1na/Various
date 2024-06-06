# Given an array arr[] of size N-1 with integers in the range of [1, N], 
# the task is to find the missing number from the first N integers.

# Note: There are no duplicates in the list.

# Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
# Output: 5
# Explanation: Here the size of the array is 8, so the range will be [1, 8]. The missing number between 1 to 8 is 5

arr = [1, 2, 4, 6, 3, 7, 8]

def missing_number(arr, n):
    sorted_arr = sorted(arr)
    # sorted_arr = [1,2,3,4,6,7,8]
    expected_arr = []
    for i in range(n):
        expected_arr.append(i+1)
        # expected_arr = [1,2,3,4,5,6,7,8]
    for j in expected_arr:
        if j not in sorted_arr:
            print(j)


missing_number(arr, 8)

def myIdioticFunction(arr, n):

    # sum all the elements of the given array:
    sum_arr = 0
    for i in arr:
        sum_arr += i
    
    # get the sum of all the numbers from 1 to n:
    expected_sum = 0
    for j in range(n+1):
        expected_sum += j
    
    # get the difference:
    difference = expected_sum - sum_arr
    return difference

print(myIdioticFunction(arr, 8))
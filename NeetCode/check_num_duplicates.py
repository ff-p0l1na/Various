# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

array_nums_1 = [1, 7, 54, 64, 6, 2, 1, 553, 99, 64, 78, 36]
array_nums_2 = [1, 7, 54, 64, 6, 2, 553, 99, 78, 36]

def checkDuplicates(nums):
    
    nums_count = {}

    for i in nums:
        if i not in nums_count:
            nums_count[i] = 1
        else:
            nums_count[i] += 1

    for v in nums_count.values():
        if v > 1:
            return True
        else:
            return False

                
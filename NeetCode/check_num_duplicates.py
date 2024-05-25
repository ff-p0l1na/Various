# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

nums = [1,2,3,3]

def checkDuplicates(nums):
    
    nums_count = {}

    for i in nums:
        if i not in nums_count:
            nums_count[i] = 1
        else:
            nums_count[i] += 1

    # nums_count = { 1: 1, 2: 1, 3: 2 }

    for v in nums_count.values():
        if v > 1:
            return True

    return False

print(checkDuplicates(nums))
        

                
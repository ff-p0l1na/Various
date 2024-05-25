# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

nums=[4,5,6]
target=10

def makeSum(nums, target):

    prevMap = {} # val : index

    for i, n in enumerate(nums):
        # i is index and n is value, 0: 4, 1:5, 2:6
        diff = target - n # 10 - 4 = 6
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i # 4:0, 5:1, 6:2
    return []

print(makeSum(nums, target))
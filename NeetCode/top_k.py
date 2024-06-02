# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

nums=[1,2]
k=2

def topKFrequent(nums, k):

    frequencies = {}
    
    for item in nums:
        if item not in frequencies:
            frequencies[item] = 1
        else:
            frequencies[item] += 1

        # frequencies={1: 1, 2: 1}

    # dict where the count is the key and the value is the list of numbers
    # reversed_frequencies = {1: [1, 2]}    

    reversed_frequencies = {}

    for k, v in frequencies.items():
        if v not in reversed_frequencies:
            reversed_frequencies[v] = [k]
        else:
            reversed_frequencies[v].append(k)





print(topKFrequent(nums, k))
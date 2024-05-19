# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

nums = [207, 1, 1, 207, 3, 32 ,65646, 3, 0, 34, 1, 1, 33, 207]
k = 2

def topkFrequency(array, int):

    # create a dict with the frequency of each element (key) being the value:
    frequency = {}

    for i in array:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1

    print(frequency)

    # create a list of frequencies:
    frequency_list = []
    for v in frequency.values():
        if v not in frequency_list:
            frequency_list.append(v)

    print(frequency_list)

    # sort the frequencies in the descending order:
    frequency_list = sorted(frequency_list, reverse=True)

    print(frequency_list)

    # find the k first elements of the sorted list (aka k most frequent):
    for x in range(k):
        value_I_want = frequency_list[x]
        for key, value in frequency.items():
            if value == value_I_want:
                print(key)

    return key

topkFrequency(nums,k)
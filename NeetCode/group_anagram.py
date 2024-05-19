# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

strs = [
    'a',
    'aaa',
    'zzz',
    'abcd',
    'dcab',
    'zzz',
    'adcb',
    'ghr'
]

def groupAnagram(array):

    anagrams = {}

    for str in array:
        sorted_str = ''.join(sorted(str))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = [str]
        else:
            anagrams[sorted_str].append(str)

    for v in anagrams.values():
        if len(v) > 1:
            print(v)
    
    return v
        
groupAnagram(strs)

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

strs=["act","pots","tops","cat","stop","hat"]

def groupAnagram(strs):

    anagrams = {}

    for str in strs:
        sorted_str = ''.join(sorted(str))
        if sorted_str not in anagrams:
            anagrams[sorted_str] = [str]
        else:
            anagrams[sorted_str].append(str)

    grouped = []
    for v in anagrams.values():
        if len(v) > 1:
            grouped.append(v)
    print(grouped)
    return grouped
        
groupAnagram(strs)

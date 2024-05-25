# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

s = 'jar'
t = 'jam'

def isAnagram(s, t):
    
    s_count = {}

    for i in s:
        if i not in s_count:
            s_count[i] = 1
        else:
            s_count[i] += 1

    # s_count = { 'j': 2, 'a': 1, 'r': 1 }

    for j in t:
        if j in s_count:
            s_count[j] -= 1
        else:
            s_count[j] = -1

    # s_count = { 'j': 1, 'a': 0, 'r': -1 }

    for v in s_count.values():
        if v == 0:
            continue
        else:
            return False

    return True
        
test = isAnagram(s, t)
print(test)

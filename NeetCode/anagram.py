# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

s = 'aaaaaaaa'
t = 'aa'

def isAnagram(string_s, string_t):
    
    s_count = {}

    for i in string_s:
        if i not in s_count:
            s_count[i] = 1
        else:
            s_count[i] += 1

    for j in string_t:
        if j in s_count:
            s_count[j] -= 1
        else:
            s_count[j] = -1

    if sum(s_count.values()) != 0:
        return False
    else:
        return True
        
test = isAnagram(s, t)
print(test)

# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters.

s = "Was it a car or a cat I saw?"

def validPalindrome(s):

    simple_s = s.lower()
    for char in simple_s:
        if not char.isalnum():
            simple_s = simple_s.replace(char, "")


    return simple_s == simple_s[::-1]

validPalindrome(s)
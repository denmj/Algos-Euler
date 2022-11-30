# Palindrome 

s = "racecar"
s2 = "race a car"
s3 = 'A man, a plan, a canal: Panama'

def is_palindrome(s: str) -> bool: 
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True



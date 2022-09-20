"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint
 substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with
 a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same
order and a new string is returned.

"""
test_str = "abbcabb"

def solution(s):
    """given a strung return its encoding"""
    sub_strings = []
    sub_sting = ""
    c = 0
    if len(s) > 0:
        sub_sting = s[0]
        c += 1
        for char in s[1:]:
            if char == sub_sting[-1]:
                c += 1
                print(c)
            sub_sting += str(c)+char
            print(sub_sting)

            c = 0
            sub_string = ""




solution(test_str)

print(test_str[-1])

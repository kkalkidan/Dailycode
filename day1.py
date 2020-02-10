"""
@Question 
Given a string, return the first recurring character 
in it,or null if there is no recurring character.
For example, given the string "acbbac", return "b".
Given the string "abcdef", return null.
"""

def recurring(string):
    checker = []

    for char in string:
        if(char in checker):
            return char
        else:
             checker.append(char)
    return None

# Testing 

assert recurring("abcb") == "b", "Error"
assert recurring("abc") ==  None, "Error"
assert recurring("aabcb") == "a", "Error"


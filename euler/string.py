

def rotations(s):
    # We can find all rotations by appending the string to itself
    ss = s + s
    for i in range(len(s)):
        yield ss[i:i+len(s)]

def palindrome(s):
    return s == s[::-1]
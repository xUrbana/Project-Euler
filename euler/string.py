
def rotations(s):
    # We can find all rotations by appending the string to itself
    ss = s + s
    for i in range(len(s)):
        yield ss[i:i+len(s)]

def palindrome(s):
    return s == s[::-1]

def pandigital(s):
    s = str(s)
    return len(s) == 10 and set('0123456789') == set(s)

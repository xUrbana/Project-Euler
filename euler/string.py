
def rotations(s):
    """Returns all possible rotations of s.
    
    For instance, rotations("hey") -> ["hey", "yhe", "eyh"]
    """
    ss = s + s
    for i in range(len(s)):
        yield ss[i:i+len(s)]

def palindrome(s):
    """Returns true if s is a palindrome, otherwise false.

    A palindrome is a string that is the same forwards and backwards.
    """
    return s == s[::-1]

def pandigital(s):
    """Returns true if s is pandigital, otherwise false.

    A pandigital string is a string that contains the digits 0-9 exactly once.
    """
    s = str(s)
    return len(s) == 10 and set('0123456789') == set(s)

from euler.integer import factorize

def euler9():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
    
    a = m^2 - n^2
    b = 2nm
    c = n^2 + m^2

    We want:
    m^2 - n^2 + 2nm + n^2 + m^2 = 1000
    2m^2 + 2nm = 1000
    2m(m + n) = 1000
    m(m + n) = 500

    Also:
    abc = (m^2 - n^2)(2nm)(n^2 + m^2)
    abc = (m^2n^2 + m^4 - n^4 -n^2m^2)(2nm)
    abc = (m^4 - n^4)(2nm)

    So we will check values of m and n that meet this condition
    """
    factors = factorize(500)

    for m,z in factors:
        n = z - m
        if m > n:
            return (m**4 - n**4) * (2*n*m)
def strWithout3a3b(A, B):
    """
    :type A: int
    :type B: int
    :rtype: str
    """
    if B > A: return strWithout3a3b(B, A)
    if A >= B * 2: return ('aab') * B + 'a' * (A - B * 2)
    return ('aab') * (A - B) + ('ab') * (B * 2 - A)

print(strWithout3a3b(4,1))

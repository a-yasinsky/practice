def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    def letters(input):
        return ''.join([c for c in input if c.isalnum()]).lower()

    symbS = letters(s)
    rev = ''
    for sym in symbS:
        rev = sym + rev
    print(rev,symbS,"0".isalnum())
    return symbS == rev

print(isPalindrome("0P"))

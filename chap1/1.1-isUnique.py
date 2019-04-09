def isUnique(str):
    return len(set(str)) == len(str)

print(isUnique("dfertxbu"))
print(isUnique("gdfgergrwwwed"))

def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

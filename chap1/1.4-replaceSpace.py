def replace(str):
    return "%20".join(str.split())

print(replace("ffg dffs wefwef     "))

def urlify(str, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(str)

    string = list(str)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return "".join(string)

print(urlify("ffg dffs wefwef     ",15))

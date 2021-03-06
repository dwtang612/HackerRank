#Given two strings, write a method to decide if one string contains a permutation of the other.

def checkPerumutation(string1, string2):
    answer = False
    if (len(string1) > len(string2)):
        longstring = string1
        shortstring = string2
    else:
        longstring = string2
        shortstring = string1
    revstring = longstring[::-1]

    for i in range(0, len(longstring) - len(shortstring)):
        if longstring[i:i+len(shortstring)] == shortstring:
            return True
        elif revstring[i:i+len(shortstring)] == shortstring:
            return True
    return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"

    print(str(checkPerumutation(s1, s2)))

#Given two strings, write a method to decide if one is a permutation of the other.

def checkPerumutation(string1, string2):
    if (len(string1) > len(string2)):
        longstring = string1
        shortstring = string2
    else:
        longstring = string2
        shortstring = string1

    
            
    return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"

    print(str(checkPerumutation(s1, s2)))

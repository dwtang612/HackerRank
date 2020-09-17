# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def isUnique(str):
    for i in str:
        if(str.count(i) >= 2):
            return "Not Unique"
    return "Unique"

if __name__ == '__main__':
    s1 = "abcdefghij"
    s2 = "aabbccddee"
    s3 = "This should be False"
    s4 = "klmoprstuv"

    print("\n")
    print("-----" + s1 + "-----")
    print("The string is: " + str(isUnique(s1)) + "\n")
    print("-----" + s2 + "-----")
    print("The string is: " + str(isUnique(s2)) + "\n")
    print("-----" + s3 + "-----")
    print("The string is: " + str(isUnique(s3)) + "\n")
    print("-----" + s4 + "-----")
    print("The string is: " + str(isUnique(s4)) + "\n")

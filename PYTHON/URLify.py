# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the 
# end to hold the additonal characters, and that you're given 
# the "true" length of the string.

# Solution 1
def URLifyEasy(str):
    return str.strip().replace(" ", "%20")

if __name__ == '__main__':
    s1 = "Mr John Smith        "
    output = "Mr%20John%20Smith"

    print(URLifyEasy(s1))

# You are given a string s and width max_width.
# Your task is to wrap the string into a paragraph of width max_width.
# <------Sample Input------>
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# 
# <------Sample Output------>
# ABCD
# EFGH
# IJKL
# MNOP
# QRST
# UVWX
# YZ

def textwrap(string, max_width):
    for length in range(0, len(string)-1, 4):
        print(string[length:length+4])
 

if __name__ == '__main__':
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wr = 4

    textwrap(str, wr)

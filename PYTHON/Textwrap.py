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
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
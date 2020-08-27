# Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# <-----Sample Input------->12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# <-----Sample Output------->

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(raw_input())
    count = 0
    list = []
    while (count < N):
        count+=1
        command = raw_input()
        job = command.split()[0]
        if (job == "insert"):
            list.insert(int(command.split()[1]), int(command.split()[2]))
        elif (job == "print"):
            print(list)
        elif (job == "remove"):
            list.remove(int(command.split()[1]))
        elif (job == "append"):
            list.append(int(command.split()[1]))
        elif (job == "sort"):
            list.sort()
        elif (job == "pop"):
            list.pop()
        elif (job == "reverse"):
            list.reverse()
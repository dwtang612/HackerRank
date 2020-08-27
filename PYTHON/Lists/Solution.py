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
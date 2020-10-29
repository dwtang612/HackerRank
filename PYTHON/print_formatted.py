def print_formatted(number):
    gap = len("{0:b}".format(number))
    for i in range(0, number):
        print("{0:{gap}d} {0:{gap}o} {0:{gap}X} {0:{gap}b}".format(i, gap=gap))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
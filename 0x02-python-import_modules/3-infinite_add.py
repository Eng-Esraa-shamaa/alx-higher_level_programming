#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summ = 0
    length = len(sys.argv) - 1
    for i in range(length):
        summ = summ + int(sys.argv[i + 1])
    print("{}".format(summ))

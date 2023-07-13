#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if (argc == 0):
        print("0 arguments.")
    elif (argc == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for c in range(argc):
        print("{}: {}".format(c + 1, sys.argv[c + 1]))

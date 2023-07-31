#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    result = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            result += 1
            if result >= x:
                break
        except (ValueError, TypeError):
            continue
    print("")
    return (result)

#!/usr/bin/python3

def safe_print_list(my_list,x):

    """
    Program that takes in a list usedz

    """
    count = int()
    for e in range(x):
        try:
            print("{}".format(my_list[e]), end="") 
            count+=1
        except IndexError:
            break
    print("")
    return count

        

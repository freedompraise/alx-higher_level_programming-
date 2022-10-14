#!/usr/bin/python3

def safe_print_list(my_list,x):

    """
    Program that takes in a list usedz

    """
    count = int()
    for e in my_list:
        try:
            print("{}".format(my_list[i]), end="") 
            count+=1
        except:
            break
    print("")
    return count

        

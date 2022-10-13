#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = int()
    for i in x:
        try:
            print(my_list[i],end ="")
            count += 1 
        except:
            break
    print("")
    return count

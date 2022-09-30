#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
end_string = ""
if int(str(number)[-1])==0:
    end_string = "0"
elif int(str(number)[-1]) > 5:
    end_string = "greater than 5"
else:
    end_string = "less than 6 and not 0"

print("Last digit of {} is {} and is {}".format(number,str(number)[-1],end_string))



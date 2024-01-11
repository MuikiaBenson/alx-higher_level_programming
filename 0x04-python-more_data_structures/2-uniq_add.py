#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set()
    result = 0

    for num in my_list:
        if num not in uniq_int:
            result += num
            uniq_int.add(num)
    return result

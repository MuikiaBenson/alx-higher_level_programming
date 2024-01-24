#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result = 0
            if isinstance(my_list_1[i], (int, float)) and \
                    isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] == 0:
                    raise ZeroDivisionError("division by 0")
                result = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError as e:
            print(e)
        except TypeError as e:
            print(e)
        finally:
            result_list.append(result)
    return result_list

#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            div = 0
            if i < len(my_list_1) and i < len(my_list_2):
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    div = my_list_1[i] / my_list_2[i]
                else:
                    print("wrong type")
            else:
                print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(div)
    return result

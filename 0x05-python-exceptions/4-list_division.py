#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                denominator = my_list_2[i]
                numerator = my_list_1[i]
                result = numerator / denominator
                if not isinstance(result, (int, float)):
                    print("wrong type")
                    result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                result_list.append(result)
    finally:
        return result_list

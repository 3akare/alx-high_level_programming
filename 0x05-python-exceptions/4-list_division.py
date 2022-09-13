#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div = 0
    new_list = []

    while (index <= list_length):
        try:
            div = my_l_1[index] / my_list_2[index]
            index += 1
        except TypeError:
            div = 0
            print("wrong type")
            index += 1
        except IndexError:
            div = 0
            print("out of range")
            index += 1
        except ZeroDivisionError:
            div = 0
            print("division by 0")
            index += 1
        finally:
            pass
        new_list.append(div)
    return (new_list)

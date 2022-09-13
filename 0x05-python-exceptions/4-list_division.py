#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div = 0
    new_list = []
    while (index < list_length):
        try:
            div = my_list_1[index] / my_list_2[index]
            index += 1
        except TypeError:
            print("{}".format("wrong type"))
            div = 0
            index += 1
        except IndexError:
            print("{}".format("out of range"))
            div = 0
            index += 1
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            div = 0
            index += 1
        except Exception:
            div = 0
            index += 1
        finally:
            new_list.append(div)
    return (new_list)

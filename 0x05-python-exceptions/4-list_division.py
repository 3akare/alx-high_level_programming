#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div = 0
    new_list = []
    while (index < list_length):
        try:
            div = my_l_1[index] / my_list_2[index]
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
        finally:
            pass
        new_list.append(div)
    return (new_list)
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
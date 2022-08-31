#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        max_number, position = 0, 0
        keys_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        for value in a_dictionary.values():
            if isinstance(value, int):
                if value > max_number:
                    max_number = value
        position = val_list.index(max_number)
        return keys_list[position]
    else:
        return None

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
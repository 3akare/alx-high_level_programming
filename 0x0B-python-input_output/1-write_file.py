#!/usr/bin/python3
def write_file(filename="",text=""):
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters

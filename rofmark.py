#!/usr/bin/python3

from rofi import Rofi
from subprocess import Popen, DEVNULL
import os
import json

r = Rofi()

bookmark_file = 'aliases.json'

def import_json(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
    return data

def bookmark_menu(data):
    rofi_list = []
    for key, _ in data.items():
        rofi_list.append(key)
    index, key = r.select('What Site?', rofi_list)
    return rofi_list[index]

data = import_json(bookmark_file)
selection_index = bookmark_menu(data)
print(data[selection_index])
Popen(['nohup', 'vivaldi-stable', data[selection_index]], stdout=DEVNULL, stderr=DEVNULL)

#!/usr/bin/python3

from rofi import Rofi
from subprocess import Popen, DEVNULL
import os
import json
import urllib.parse

r = Rofi()

# use xdg-open if you want, mine is fucked up though, so i'll just set it like this
browser_path = "vivaldi-stable"
bookmark_file = os.environ['HOME'] + '/aliases.json'
search_string = 'https://duckduckgo.com/?q='


def import_json(file):
    with open(file, "r") as read_file:
        data = json.load(read_file)
    return data


def bookmark_menu(data):
    # start out with only the search option
    rofi_list = []
    # iterate and add in all of the alias items
    for key, _ in data.items():
        rofi_list.append(key)
    # store the index and key of the selection for retrieval
    result = r.select('What Site?', rofi_list, rofi_args=['-fuzzy'])
    if type(result) is str:
        return(result)
    else:
        key = result[0]
    if key < 0:
        return False
    return rofi_list[key]


data = import_json(bookmark_file)
selection_index = bookmark_menu(data)

if data.get(selection_index):
    Popen(['nohup', browser_path, data[selection_index]],
          stdout=DEVNULL, stderr=DEVNULL)
else:
    Popen(['nohup', browser_path, search_string + selection_index],
          stdout=DEVNULL, stderr=DEVNULL)

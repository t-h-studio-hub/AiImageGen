import json
import os

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

demos_json = read_json_file("online/demos.json")
tools_json = read_json_file("online/tools.json")

demos_dict = {}
for name, values in demos_json.items():
    demos_dict[name] = values
tools_dict = {}
for name, values in tools_json.items():
    tools_dict[name] = values


demos_names = []
tools_names = []
def load_demos_names():
    for _ in demos_dict.keys():
        demos_names.append(_)
    return demos_names
def load_tools_names():
    for _ in tools_dict.keys():
        tools_names.append(_)
    return tools_names

def load_demos_url(name):
    return demos_names[name][0]
def load_tools_url(name):
    return tools_names[name][0]


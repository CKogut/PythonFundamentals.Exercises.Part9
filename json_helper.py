import json
import os


# reads a json file and returns a dictionary
def read_json(file_name):
    with open(file_name) as f:
        x = json.load(f)

    return x


# takes a dir name and returns a list of dictionaries of the json files
def read_all_json_files(dir_name):
    my_list = []

    for name in os.listdir(dir_name):
        path = os.path.join(dir_name, name)

        if os.path.isfile(path):
            my_list.append(read_json(path))
    return my_list


def write_pickle():



# y = read_json('data/super_smash_bros/link.json')
# print(y)
# print(type(y))

z = read_all_json_files('data/super_smash_bros')
print(z)
print(type(z))

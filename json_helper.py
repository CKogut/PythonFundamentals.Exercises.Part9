import json
import os
import pickle


# reads a json file and returns a dictionary
def read_json(file_name):
    with open(file_name) as f:
        return json.load(f)


# takes a dir name and returns a list of dictionaries of the json files
def read_all_json_files(dir_name):
    my_list = []

    for name in os.listdir(dir_name):
        path = os.path.join(dir_name, name)

        if os.path.isfile(path):
            my_list.append(read_json(path))
    return my_list


def write_pickle(file_path, data):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data


y = read_json('data/super_smash_bros/link.json')
print(y)
print(type(y))


z = read_all_json_files('data/super_smash_bros')
print(z)
print(type(z))

write_pickle('super_smash_characters.pickle', z)
zz = load_pickle('super_smash_characters.pickle')
print(zz)
print(type(zz))


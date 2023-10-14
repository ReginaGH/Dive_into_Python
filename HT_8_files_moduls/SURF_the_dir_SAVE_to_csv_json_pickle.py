import os
import json
import csv
import pickle

__all__ = ['save_to_file', 'bypass_the_dir']

"""
Function bypass the dir
receive the way to directory and bypass the dirs an files and return list of lists
which contains: 
1) if it's directory: [dir_name, type_of_object, size_of_dirs_and_files_inside]. Dirs_name would be two if it has parents dir
2) if it's file: [file_name, type_of_object, size_of_object]
Function save_to_file
save to 3 types of files: json, csv, pickle
receive way to use in the function 'bypass_the_dir' """


def save_to_file(dir_address):
    with (
        open('../HT_8_files_moduls/json_dir_contains', 'w', encoding='utf-8') as json_file,
        open('../HT_8_files_moduls//csv_dir_contains', 'w', newline='') as csv_file,
        open('../HT_8_files_moduls//bin_dir_contains', 'wb') as pickle_file
    ):
        json.dump(bypass_the_dir(dir_address), json_file, indent=2),
        csv_write = csv.writer(csv_file)
        csv_write.writerows(bypass_the_dir(dir_address))
        pickle.dump(bypass_the_dir(dir_address), pickle_file)


def bypass_the_dir(dir_address):
    d = 'directory'
    f = 'file'
    directory = []
    files = []
    for dir_path, dir_name, file_name in os.walk(way):
        directory.append(dir_name)
        files.append(file_name)
    for i in range(len(directory)):
        dir_sum = 0
        if i == 0:
            first_list = list()
            first_list.append([directory[i][0], d])
            for j in range(len(files[i])):
                dir_sum += files[i][j].__sizeof__()
                first_list.append([files[i][j], f, files[i][j].__sizeof__()])
            first_list[0].append(dir_sum)
            return first_list
        else:
            new_list = list()
            new_list.append([directory[i - 1][0], directory[i], d])
            for j in range(len(files[i])):
                new_list.append([files[i][j], f, files[i][j].__sizeof__()])
                dir_sum += files[i][j].__sizeof__()
            new_list[0].append(dir_sum)
            return new_list


if __name__ == '__main__':
    save_to_file(os.getcwd())

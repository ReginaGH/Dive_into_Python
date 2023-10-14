import os

__all__ = ['rename_files']

""" Function "rename files"
receive: 
- address - address to directory , 
- save_name_limits - list with two numbers - which part of original name should be save ,
- add_name - new part of name to add ,
- counter - how many digits will be in new file name to count files
- in_extension - to recognize which files should be rename,
- out_extension - to change type of file 
function rename files in the directory"""


def rename_files(address, save_name_limits: list|tuple, add_name: str, counter: int, in_extension: str, out_extension):
    order = []
    for i in range(1, 10 ** counter):
        order.append(i)
    order.reverse()
    for ways, dirs, files in os.walk(address):
        for f in files:
            old_name = f
            print(f'{f = } {type(f)}')
            if f.split('.')[1] == in_extension:
                f_name, f_ext = f.split('.')[0], f.split('.')[1]
                new_name = f_name[save_name_limits[0]-1:save_name_limits[1]-1] + add_name + str(order.pop()) + '.' + out_extension
                os.rename(os.path.join(address, old_name), os.path.join(address, new_name))


if __name__ == '__main__':
    rename_files('../../Seminar_7', [1, 3], '_sem7_file', 3,'txt', 'md')

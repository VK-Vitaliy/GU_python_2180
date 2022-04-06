# Написать скрипт, создающий стартер (заготовку) для проекта со структурой папок.
import os

folder_names = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
new_path = 'C:/temp/'
root = [k for k in folder_names.keys()]
if not os.path.exists(os.path.join(new_path, root[0])):
    os.chdir(new_path)
    os.mkdir(root[0])
new_path += (os.path.join(root[0]))
for second_folders in folder_names.values():
    for folder in second_folders:
        if not os.path.exists(os.path.join(new_path, folder)):
            os.chdir(new_path)
            os.mkdir(folder)

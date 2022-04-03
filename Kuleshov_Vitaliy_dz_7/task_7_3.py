# Написать скрипт, который собирает все шаблоны в одну папку templates
import os
import shutil

templates_folder = os.path.join('my_project', 'templates')
if not os.path.exists(templates_folder):
    os.mkdir(templates_folder)

folder = os.path.join('my_project')
files_list = []

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('.html'):
            files_list.append(os.path.join(root, file))

for path in files_list:
    folder = os.path.join(templates_folder, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    if not os.path.isfile(save_path):
        shutil.copy(path, save_path)

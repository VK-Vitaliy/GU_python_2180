import os
import json


def create_library(library_template, prefix=''):
    for root_dir, second_dir in library_template.items():
        folder = os.path.join(prefix, root_dir)
        os.makedirs(folder, exist_ok=True)
        if isinstance(second_dir, dict):
            create_library(second_dir, folder)
        else:
            for el in second_dir:
                if isinstance(el, dict):
                    create_library(el, folder)
                elif isinstance(el, str):
                    with open(os.path.join(folder, f'{el}'), 'w') as _temp:
                        pass


# заготовка для проекта хранится в файле config.json в виде словаря.
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

create_library(config)

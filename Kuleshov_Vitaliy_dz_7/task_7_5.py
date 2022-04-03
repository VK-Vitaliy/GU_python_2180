# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>])
import os
import json

folder = os.getcwd()
key = []
for root, dirs, files in os.walk(folder):
    if not files:
        continue
    key.extend(
        [[os.path.getsize(os.path.join(root, name)), name.split('.')[-1] if name.count('.') else ''] for name in files])

sizes, extension = list(zip(*key))

bins = [10 ** i for i in range(2, len(str(max(sizes))) + 1)]
dict_size_ext = {}
for size, ext in key:
    for j in bins:
        if size < j:
            len_saved, ext_saved = dict_size_ext.get(j, (0, []))
            len_saved += 1
            if ext not in ext_saved:
                ext_saved.append(ext)
            dict_size_ext.update({j: (len_saved, ext_saved)})

result = dict(sorted(dict_size_ext.items()))
print(result)
with open(os.path.join(folder, '_summary.json'), 'w') as f:
    json.dump(result, f)

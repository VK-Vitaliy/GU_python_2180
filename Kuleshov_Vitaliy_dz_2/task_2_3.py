# 3. Решить задачу 2 не создавая новый список
dz_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
skip_quotes = False
print(id(dz_list))  # проверяем id списка
for i in dz_list[:]:
    dz_list.remove(i)
    if i.isdigit():
        dz_list.extend(['"', i.zfill(2), '"'])
    elif i[1:].isdigit() and i[0] == '+' or i[0] == '-':
        dz_list.extend(['"', i.zfill(3), '"'])
    else:
        dz_list.append(i)
print(dz_list)
print(id(dz_list))  # проверяем id списка, id не изменился

for i in dz_list[:]:
    dz_list.remove(i)
    dz_list.append(i)
    if i == '"' and not skip_quotes:
        skip_quotes = True
    elif i == '"' and skip_quotes:
        skip_quotes = False
        dz_list.append(' ')
    elif i != '"' and not skip_quotes:
        dz_list.append(' ')

print(dz_list)
print(id(dz_list)) # проверяем id списка, id не изменился

print(''.join(dz_list))
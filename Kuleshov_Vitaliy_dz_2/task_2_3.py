# 3. Решить задачу 2 не создавая новый список
dz_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(dz_list))
for i in dz_list[:]:
    if i.isdigit():
        n = int(i)
        n = f'"{n:02d}"'
        idx = dz_list.index(i)
        dz_list.remove(i)
        dz_list.insert(idx, n)
    elif i[0] == '+' and i[1].isdigit():
        n = int(i)
        n = f'"+{n:02d}"'
        idx = dz_list.index(i)
        dz_list.remove(i)
        dz_list.insert(idx, n)
    elif i[0] == '-' and i[1].isdigit():
        n = int(i)
        n = f'"{n:02d}"'
        idx = dz_list.index(i)
        dz_list.remove(i)
        dz_list.insert(idx, n)
print(id(dz_list))
print(' '.join(dz_list))
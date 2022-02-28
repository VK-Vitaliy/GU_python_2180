dz_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in dz_list[:]:
    if i.isdigit():
        n = int(i)
        n = f'{n:02d}'
        idx = dz_list.index(i)
        dz_list.remove(i)
        dz_list.insert(idx, '"')
        dz_list.insert(idx, n)
        dz_list.insert(idx, '"')
    elif i[0] == '+' or i[0] == '-' and i[1].isdigit():
        n = int(i)
        n = f'{n:02d}'
        idx = dz_list.index(i)
        dz_list.remove(i)
        dz_list.insert(idx, '"')
        dz_list.insert(idx, n)
        dz_list.insert(idx, i[0])
        dz_list.insert(idx, '"')

print(dz_list)
result = ' '.join(dz_list) # не получается убрать пробелы между ковычками и числами
print(type(result))

print(result)


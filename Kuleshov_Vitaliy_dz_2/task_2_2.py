dz_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for i in dz_list[:]:
    if i.isdigit():
        new_list.extend(['"', i.zfill(2), '"'])
    elif i[1:].isdigit() and i[0] == '+' or i[0] == '-':
        new_list.extend(['"', i.zfill(3), '"'])
    else:
        new_list.append(i)
print(new_list)

list_answer = []
skip_quotes = False

for i in range(len(new_list)):
    list_answer.append(new_list[i])
    if new_list[i] == '"' and not skip_quotes:
        skip_quotes = True
    elif new_list[i] == '"' and skip_quotes:
        skip_quotes = False
        list_answer.append(' ')
    elif new_list[i] != '"' and not skip_quotes and i + 1 != len(new_list):
        list_answer.append(' ')

print(list_answer)

print(''.join(list_answer))

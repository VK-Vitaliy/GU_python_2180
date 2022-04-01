# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    list_tuples = []
    for line in f:
        remote_addr = line.split(' ')[0]
        remote_type = line.split(' ')[5].strip('"')
        requested_resource = line.split(' ')[6]
        list_tuples.append((remote_addr, remote_type, requested_resource))
    for i in range(len(list_tuples)):
        print(list_tuples[i])

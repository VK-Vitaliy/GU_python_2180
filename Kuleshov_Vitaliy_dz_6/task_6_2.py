# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_address = []
    for line in f:
        remote_addr = line.split(' ')[0]
        ip_address.append(remote_addr)

    dict_ip = {}
    for ip in ip_address:
        if ip in dict_ip:
            dict_ip[ip] += 1
        else:
            dict_ip[ip] = 1

    max_value = max(dict_ip.values())
    spammer = {ip: total for ip, total in dict_ip.items() if total == max_value}
    for ip, total in spammer.items():
        print(f'IP адрес: {ip}, количество запросов - {str(total)}')

# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
import re


def log_parse(scr):
    remote_addr = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}').findall(scr)
    request_datetime = re.compile(r'(\d{2}/.*/\d{4}(?::\d{2}){3}.\+\d{4})').findall(scr)
    request_type = re.compile(r'\"([A-Z]{3,5})').findall(scr)
    requested_resource = re.compile(r'\/\w+/\w+\_\d+').findall(scr)
    response_code = re.compile(r'\s([0-9]{3})\s').findall(scr)
    response_size = re.compile(r'\s[0-9]{3}\s(\d+)').findall(scr)

    parsed_raw = tuple(
        x[0] for x in [remote_addr, request_datetime, request_type, requested_resource, response_code, response_size])
    return parsed_raw


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(log_parse(line))

import re


def email_parse(email_address):
    RE_EMAIL = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
    if re.match(RE_EMAIL, email_address):
        result_dict = dict()
        result_dict['username'] = re.split('@', email_address)[0]
        result_dict['domain'] = re.split('@', email_address)[1]
        return result_dict
    else:
        msg = f'wrong email: {email_address}'
        raise ValueError(msg)


print(email_parse('kulvitall.vk@gmail.com'))

import requests
from datetime import datetime


def currency_rates(currency):
    """
    param currency: the alphabetic currency code
    return: currency conversion rates to ruble
    """
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.text
    values = []
    char_code = []
    for el in content.split('<Value>')[1:]:
        values.append(round(float(el.split('</Value>')[0].replace(',', '.')), 2))

    for el in content.split('<CharCode>')[1:]:
        char_code.append(el.split('</CharCode>')[0])

    currency_dict = dict(zip(char_code, values))
    date = datetime.now().strftime('%Y-%m-%d')

    if currency_dict.get(currency.upper()):
        return f'{currency_dict.get(currency.upper())}, {date}'
    else:
        return None


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))
    print(currency_rates('123'))

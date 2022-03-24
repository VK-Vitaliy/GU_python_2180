import requests
from datetime import datetime


def currency_rates(currency):
    """
    param currency: the alphabetic currency code
    return: currency conversion rates to ruble
    """
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.text
    result = None
    date = datetime.now().strftime('%Y-%m-%d')
    if currency.upper() not in content:
        return result
    else:
        for el in content.split(f'{currency.upper()}')[1:]:
            for el_1 in el.split('</Value>')[:1]:
                result = round(float(el_1.split('<Value>')[1].replace(',', '.')), 2)
                return f'{result}, {date}'


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('eur'))

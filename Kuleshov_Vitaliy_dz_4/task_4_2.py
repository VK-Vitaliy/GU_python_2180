import requests


def currency_rates(currency):
    """
    param currency: the alphabetic currency code
    return: currency conversion rates to ruble
    """
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.text
    result = None
    if currency.upper() not in content:
        return result
    for el in content.split(f'{currency.upper()}')[1:]:
        for el_1 in el.split('</Value>')[:1]:
            result = round(float(el_1.split('<Value>')[1].replace(',', '.')), 2)
            return result


print(currency_rates("USD"))
print(currency_rates('eur'))
print(currency_rates('GBP'))

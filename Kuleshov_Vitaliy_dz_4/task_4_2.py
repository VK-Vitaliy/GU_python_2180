import requests


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

    return currency_dict.get(currency.upper())


print(currency_rates("USD"))
print(currency_rates('EUR'))

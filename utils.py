
from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

def currency_rates(code):
    my_stroka = content.split("<Valute ID=")
    for i in my_stroka:
        if code.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))

if __name__ == "__main__":
    print(currency_rates("EUR"))
from bs4 import BeautifulSoup
import requests
n = 1


def real_price(stock_code):

    url = f'https://in.finance.yahoo.com/quote/{stock_code}?p={stock_code}&.tsrc=fin-srch'
    r = requests.get(url)

    get_price = BeautifulSoup(r.text, "html.parser")
    get_price = get_price.find('div', class_="D(ib) Va(m) Maw(65%) Ov(h)")
    get_price = get_price.find('span').text
    get_price = get_price.replace(',', '')
    get_price = float(get_price)
    return get_price


# code = str(input())
# levels = float(input("enter the levels"))
print(real_price(AAPL))
print(1)

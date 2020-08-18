import requests  # pip install requests
from bs4 import BeautifulSoup as bs  # pip install beautifulsoup4


def retrieve_google_shopping_prices(url, class_name):
    response = requests.get(url)
    soup = bs(response.content)
    prices = soup.findAll('span', attrs={"class": class_name})
    return list(map(lambda x: float(__retrieve_float(x)), prices))


def __retrieve_float(x):
    return x.text.replace("\xa0", "").replace("€", "").replace(",", ".")

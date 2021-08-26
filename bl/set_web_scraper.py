# Import Module
from bs4 import BeautifulSoup
import requests

# Assing website
import requests


# Function to find tags
def GetSetData(set):
    result = ''
    for item in set:
        print(item)
        URL = "https://marketdata.set.or.th/mkt/stockquotation.do?symbol=" + \
            item + "&language=th&country=TH"
        html = requests.get(URL)

        # parse html content
        soup = BeautifulSoup(html.content, "html5lib")

        # find tags by CSS class
        latestPrice = soup.find("td", class_="set-color-green")
        if(latestPrice is None):
            latestPrice = soup.find("td", class_="set-color-red")
        if(latestPrice is None):
            latestPrice = soup.find("td", class_="set-color-black")

        result = result + "\n ราคาหุ้น {0} ราคา {1}".format(item.upper(), latestPrice.text.strip())
    
    return str(result)

import requests
from bs4 import BeautifulSoup


def ekstraksi_data():

    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")

    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None



    print(content.status_code)
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        title = soup.find('title')
        print(title.string)


if __name__ = '__main__':
    print('ini adalah package gempa terkini')
    print('hai')
import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
       return None

    if content.status_code == 200:
        print(content.text)
        return content.text



def tampilkan_data(result):
    if result is None:
        print("Sorry the data could not be displayed")
    else :
        print("Ok.... Done. All data is displayed successfully")








# if __name__ == '__main__':
#     print('ini adalah package gempa terkini')
#     print('hai')
import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
       return None

    # Mengambil title
    # if content.status_code == 200:
    #     soup = BeautifulSoup(content.text, 'html.parser')
    #     title = soup.find('title')
    #     print(title.string)
    #     return title

    # mengambil tanggal
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        # tanggal = soup.find('span', {'class': 'waktu'})
        # waktu = tanggal.text.split(', ')[1]
        # tanggal = tanggal.text.split(', ')[0]



        # Kode yang lebih sederhana

        result = soup.find('span', {'class', 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        return hasil



def tampilkan_data(result):
    if result is None:
        print("Sorry the data could not be displayed")

    print(f"Tanggal :  {result['tanggal']}")
    print(f"Waktu :  {result['waktu']}")











# if __name__ == '__main__':
#     print('ini adalah package gempa terkini')
#     print('hai')
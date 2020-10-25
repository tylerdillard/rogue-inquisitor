from bs4 import BeautifulSoup
import requests
import urllib
import os
from urllib.parse import urlparse

archive_url = 'https://thetrove.is/Books/Dungeons%20%26%20Dragons%20%5Bmulti%5D/5th%20Edition%20%285e%29/Core/'
r = requests.get(archive_url, timeout=5)
soup = BeautifulSoup(r.content, 'html.parser')
cells = soup.find_all('td', {'class': 'link'})[1:]

for td in cells:
    book_path = (td.a['href'])
    book_name = (td.text)
    download_url = urllib.parse.urljoin(archive_url, book_path)
    d = requests.get(download_url, stream=True)
    
    with open('C:/Users/Tyler/Documents/5e/Core/'+ book_name, 'wb') as f :
        f.write(d.content)
        print('downloading ' + book_name)

print('sleight of hand check successful')
from bs4 import BeautifulSoup
import requests
import os
import urllib
from urllib.parse import urlparse

download_url = 'https://thetrove.is/Books/Dungeons%20%26%20Dragons%20%5Bmulti%5D/5th%20Edition%20%285e%29/Core/Xanathar%27s%20Guide%20to%20Everything.pdf'
r = requests.get(download_url, stream=True)
a = urlparse(download_url)
book_name = (os.path.basename(a.path))

with open('C:/Users/Tyler/Documents/5e/Core/'+ book_name, 'wb') as f :
   f.write(r.content)

print('sleight of hand check successful')
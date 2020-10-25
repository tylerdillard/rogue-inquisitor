from bs4 import BeautifulSoup
import requests
import urllib

archive_url = 'https://thetrove.is/Books/Dungeons%20%26%20Dragons%20%5Bmulti%5D/5th%20Edition%20%285e%29/Core/'
r = requests.get(archive_url, timeout=5)
soup = BeautifulSoup(r.content, 'html.parser')
cells = soup.find_all('td', {'class': 'link'})
    
for td in cells:
    books = (td.a['href'])
    download_url = urllib.parse.urljoin(archive_url, books)

print(download_url)
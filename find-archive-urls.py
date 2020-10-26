from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urlparse
from investigate import investigate
from downloadScroll import downloadScroll

game_url = 'https://thetrove.is/Books/Dungeons%20%26%20Dragons%20%5Bmulti%5D/5th%20Edition%20%285e%29/'
r = requests.get(game_url, timeout=5)
soup = BeautifulSoup(r.content, 'html.parser')
cells = soup.find_all('td', {'class': 'link'})[1:]

for td in cells:
    archive_path = (td.a['href'])
    archive_name = (td.text)
    archive_url = urllib.parse.urljoin(game_url, archive_path)
    
    if archive_url[-1] == '/':
        investigate(archive_url)
    
    else:
        downloadScroll(archive_url, archive_name)

print('Library pilfered')
from bs4 import BeautifulSoup
import requests

base_url = 'https://thetrove.is/Books/Dungeons%20%26%20Dragons%20%5Bmulti%5D/5th%20Edition%20%285e%29/Core/'
response = requests.get(base_url, timeout=5)
soup = BeautifulSoup(response.content, 'html.parser')
cells = soup.find_all('td', {'class': 'link'})

for td in cells:
    links = (td.a['href'])
    print(links)
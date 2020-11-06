from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urlparse
import os
from time import sleep
from downloadScroll import downloadScroll

def investigate(archive_url):
    
    #get relevant table cell content ignoring /Parent Directory
    r = requests.get(archive_url, timeout=5)
    soup = BeautifulSoup(r.content, 'html.parser')
    cells = soup.find_all('td', {'class': 'link'})[1:]

    for td in cells:
        #find links and link names
        scroll_path = (td.a['href'])
        scroll_name = (td.text)
        download_url = urllib.parse.urljoin(archive_url, scroll_path)
        
        if scroll_path[-1] == '/': 
            #identify child folders, then continue investigating down folder rabbit hole
            print('investigating '+ scroll_name)            
            investigate(download_url)
        
        else:
            downloadScroll(download_url, scroll_name)
      
print('investigation check successful')
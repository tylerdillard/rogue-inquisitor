from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urlparse
from time import sleep
import os

def downloadScroll(download_url, scroll_name):

    print('downloading ' + scroll_name)
    raw_directory = urlparse(download_url)
    pretty_directory = urllib.parse.unquote_plus(raw_directory.path)
    
    print(raw_directory)
    print(pretty_directory)

    #d = requests.get(download_url, stream=True)
    
    #with open('C:/Users/Tyler/Documents'+pretty_directory 'wb') as f :
        #f.write(d.content)
    
    #sleep(2)

#print('sleight of hand check successful')
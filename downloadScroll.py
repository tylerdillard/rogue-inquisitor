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
    split_directory = pretty_directory.split('/')[2:-1]
    split_filepath = pretty_directory.split('/')[2:]
    joined_directory = '/'.join(split_directory)
    joined_filepath = '/'.join(split_filepath)
    save_directory = 'C:/Users/Tyler/Documents/'+joined_directory
    save_filepath = 'C:/Users/Tyler/Documents/'+joined_filepath

    #check_folder = os.path.isdir(save_directory)
    #if not check_folder:
        #os.makedirs(save_directory)
    
    #d = requests.get(download_url, stream=True)
    
    #with open(save_filepath, 'wb') as f :
        #f.write(d.content)
    
    #sleep(2)

#downloadScroll(download_url, scroll_name)
print('sleight of hand check successful')
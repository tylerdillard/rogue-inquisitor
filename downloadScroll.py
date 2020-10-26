from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urlparse
from time import sleep
import os
from clean_scroll_name import clean

def downloadScroll(download_url, scroll_name):
    
    print('downloading ' + clean(scroll_name))
    
    #create a pretty name for saved folders and files
    raw_directory = urlparse(download_url)
    pretty_directory = urllib.parse.unquote_plus(raw_directory.path)
    split_directory = pretty_directory.split('/')[2:-1]
    joined_directory = '/'.join(split_directory)
    save_directory = 'C:/Users/Tyler/Documents/'+joined_directory
    save_filepath = save_directory + '/' + clean(scroll_name)
    
    #check if the destination already been created, and if not create one
    check_folder = os.path.isdir(save_directory)
    if not check_folder:
        os.makedirs(save_directory)
    
    #check if the file has already been downloaded
    check_file = os.path.isfile(save_filepath)
    if check_file:
        print('you already swiped this scroll: '+scroll_name)
    
    #download the file
    else:
        d = requests.get(download_url, stream=True)
    
        with open(save_filepath, 'wb') as f :
            f.write(d.content)

print('sleight of hand check successful')
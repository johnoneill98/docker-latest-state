# This code takes info from the API and lets the user to search for a specifc image or list all the images
import json
import requests

def search(ui):
    url = 'https://hub.docker.com/v2/repositories/library/'
    response = requests.get(url+ui+'/')
    data = json.loads(response.text)
    desc = data['full_description']
    line  = desc.split('\n')
    for text in line:
        if 'latest' in text:
            left = '[`'
            right = '`,'
            version = text[text.index(left)+len(left):text.index(right)]
            print ("Version is: "+version)
            break

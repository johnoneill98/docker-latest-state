# This code takes info from the API and lets the user to search for a specifc image or list all the images
import json
import urllib.request

url = 'https://hub.docker.com/v2/repositories/library/?page=1&page_size=100'
json_obj = urllib.request.urlopen(url)
data = json.load(json_obj)
def search(ui):
    found = False
    ui = ui.replace(' ', '-')
    for item in data['results']:
        if item['name'] == ui:
            print(item['name'])
            print(item['description'])
            print("Last updated on " + item['last_updated'])
            found = True
            break
    if not found:
        print("Not found, try again")
def list():
    for item in data['results']:
        print(item['name'])

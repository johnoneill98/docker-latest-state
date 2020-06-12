# This code takes info from the API and lets the user to search for a specifc image or list all the images
import json
import requests

def search(ui):
    url = "https://hub.docker.com/v2/repositories/library/"
    ui = ui.replace(' ','-' )
    response = requests.get(url+ui+'/')
    try:
        data = json.loads(response.text)
        desc = data['full_description']
        lDesc = desc.split('\n')
        lDesc = list(filter(lambda x: 'latest' in x,lDesc))
        lDesc = lDesc[0].split(',')
        sDesc =(lDesc[0].split('`')[1].split(lDesc[0])[0])
        sDesc2 =(int(sDesc[0]))
        print(sDesc)

#  Error Handling
    except KeyError as err:
        print("Can not find image")
    except ValueError as err:
        print("Can not find the latest version of the image")

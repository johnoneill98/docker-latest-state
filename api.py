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
        print("Latest version of "+ ui + " is " + sDesc)


#  Error Handling
    except KeyError as err:
        print("Can not find image")
    except ValueError as err:
        print("Can not find the latest version of the image")

def printNumber(name,number):
    url = "https://hub.docker.com/v2/repositories/library/"
    ui = name.replace(' ','-' )
    response = requests.get(url+ui+'/')
    number2 = "`" +number +'`'
    try:
        data = json.loads(response.text)
        desc = data['full_description']
        Desc1 = desc.split('\n')
        found = False
        for l in Desc1:
            if number2 in l:
                found = True
                if 'latest' in l:
                    print("Version: "+ number + " is the latest version of "+ name)
                else:
                    print("Version: "+ number + " is a valid of "+ name)
                break
        if not found:
            print("Version: " + number + " is not a valid version of " + name )
            search(name)

    except KeyError as err:
        print("Can not find image")
    except ValueError as err:
        print("Can not find the latest version of the image")
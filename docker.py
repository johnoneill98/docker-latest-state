import sys
import argparse
import json
import requests

def api(image):
    url = "https://hub.docker.com/v2/repositories/library/"
    ui = image.replace(' ', '-')
    response = requests.get(url+ui+'/')
    data = json.loads(response.text)
    desc = data['full_description']
    desc1 = desc.split('\n')
    return desc1

def main():
    parser = argparse.ArgumentParser(
        description='This script takes a image and either shows the latest version of the image or if the version is a valid version'
    )
    parser.add_argument('--image', '-i', dest='image', type=str,
                        help= 'Please enter a image name.')

    parser.add_argument('--version', '-v', dest='version', type=str,
                        help= 'Please enter a version number to see if it is valid or not.')
    args = parser.parse_args()

    if args.image:
        try:
            args.image = args.image.lower()
            image = api(args.image)
            desc1 =list(filter(lambda x: 'latest' in x, image))
            desc1 = desc1[0].split(',')
            sDesc =(desc1[0].split('`')[1].split(desc1[0])[0])
            sDesc2 = (int(sDesc[0]))
            print("Latest version of " + args.image+ " is " + sDesc)
        except KeyError as err:
            print("Can not find image")
        except ValueError as err:
            print("Can not find the latest version of the image")
    if args.version:
        try:
            number = args.version
            number2 = '`'+ number + '`'
            found = False
            for l in image:
                if number2 in l:
                    found = True
                    if 'latest' in l:
                        print("Version: " + number +" is the latest version"+ args.image)
                    else:
                        print("Version: " + number + " is a valid version of "+ args.image)
                    break
            if not found:
                print("Version: " + number + " is not a valid version of" +args.image)
        except UnboundLocalError as err:
            print("You must put an image name first then the version number")
main()

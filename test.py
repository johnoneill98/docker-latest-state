"""
ASSUMPTIONS: The latest version is the last updated
             The version only contiains integers and decimals
"""
import argparse
import requests
from operator import itemgetter
def validVersion(vname):
    """[summary]
    This function takes the version number of an images and tells if its a valid version or not.
    If the version has words in ti then it is is valid

    Args:
        vname: the name of the version

    Returns:
        A boolean value that tells if teh version number is valid or not based on
        if the version numbers has only numbers and decimals or not
    """
    isValid= True
    for s in vname:
        if not (s.isnumeric() or s == '.'):
            isValid = False
            break
    return isValid

def api(image):
    """[summary]
    User sumbits an image name and it will contact the api endpoint to retrive all the version that docker supports
    Args:
        image from dockerHub

    Returns:
        a list of all version of the supported  images from dockerHub
    """
    # intital api call
    url = 'https://registry.hub.docker.com/v2/repositories/library/'
    #replaces all spaces with dashes to satisfy teh api call
    ui = image.replace(" ", "-")
    # complete api call
    response = requests.get(f"{url}/{ui}/tags?page=1&page_size=25")
    response = response.json()
    response = response['results']
    names ={ }
    for l in response:
        vname =l['name']
        # formating the date for it to be easier to read
        last_updated = l['last_updated'].replace('T', ' ')
        if validVersion(vname):
            values={last_updated:vname}
            names.update(values)
    # list of tuples from earliest and latest
    new_list=(sorted(names.items(), key = lambda kv: (kv[0], kv[1])))
    print(new_list)
    return new_list
def latest(image):
    # finds out what is the latest version of an image
    versions = api(image)
    print("Latest version of " + image + " is " + versions[-1][-1])
def version(image, number):
    # see if a version is valid or not, if it isn't it wil give a lists of valid versions
    versions = api(image)
    #itemgetter takes the list of tuples  and returns every value at index 1 for each tuple
    result = list(map(itemgetter(1), versions))
    if number not in result:
         print('Version: '+ number + ' is not a valid version of ' +image)
         print('Valid versions of ' +image + ' are')
         print(result)
    else:
        print('Version ' + 'number is a valid version of '  + image )
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This script takes a image and either shows the latest version of the image or if the version is a valid version'
    )
    parser.add_argument('-i', dest='image', type=str, required=True,
                        help= "Please enter a image")
    parser.add_argument('-v', dest='version', type=str,
                        help= "Please enter a image then its version number ")
    args = parser.parse_args()
    if args.image:
        latest(args.image)
    if args.version:
        version(args.image, args.version)

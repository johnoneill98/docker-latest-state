
import argparse
import requests
from operator import itemgetter
import sys
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
    isvalid= True
    for s in vname:
        if not (s.isnumeric() or s == '.'):
            isvalid = False
            break
    return isvalid

def api(image):
    """[summary]
    User sumbits an image name and it will contact the api endpoint to retrive all the version that docker supports
    Args:
        image from dockerHub

    Returns:
        a list of all version of the supported  images from dockerHub
    """
    #replaces all spaces with dashes to satisfy the api call
    ui = image.replace(" ", "-")
    # complete api call
    if ui.find("/") != -1:
        url = "https://registry.hub.docker.com/v2/repositories/"
    else:
        url = "https://registry.hub.docker.com/v2/repositories/library/"
    response = requests.get(f"{url}/{ui}/tags?page=1&page_size=100")
    # Error checking
    if response.status_code != 200:
        print(f"Error {image} does not have any infomarion about version numbers")
        quit()
    response = response.json()
    if response["results"] == []:
        print(f"Error{ui}does not hae any information about version numbers")
    response = response["results"]
    return response
def manipulate(response) :
    names ={ }
    test =[]
    for l in response:
        vname =l["name"]
        last_updated=l["last_updated"]
        test.append(last_updated)
        if last_updated == None:
            test.remove(last_updated)
        # formating the date for it to be easier to read
        last_updated = str(test).replace("T", " ")
        if validVersion(vname):
            values={last_updated:vname}
            names.update(values)
    # list of tuples from earliest and latest
    new_list=(sorted(names.items(), key = lambda kv: (kv[0], kv[1])))
    #itemgetter takes the list of tuples  and returns every value at index 1 for each tuple
    new_list = list(map(itemgetter(1), new_list))
    if new_list == []:
        raise IndexError(f" image does not exist")
    return new_list
def last_updated(image, update):
    # finds out what is the latest version of an image
    print(f"Last updated version of {image} is {update[-1]}")

def version_list(name, image, number):
    # see if a version is valid or not, if it isn't it wil give a lists of valid versions
    if number not in image:
         print(f"Version: {number} is not a valid version of  {name}")
         print(f"Valid versions of {name} are")
         print(f"{image}")
    else:
        print(f"Version {number} is a valid version of {name}")
def last_version(image,versions):
    """[summary]
    Takes the list of valid version numbers and conversts it to a number in order to sort for lowest to highest
    Args:
        image ([type]): [a valid version name]
    """
    finallist =[]
    for v in versions:
        versionNumberList = v.split(".")
        y = 0.0
        for i,n in enumerate(versionNumberList):
            y = y+(int(n)/(10**i))
        finallist.append((y,v))
    finallist.sort( reverse = True)

   # printing(image,finallist[0][1])
    print(f"The latest version of {image} is {finallist[0][1]}")

def printing(a,b):
    if last_version:
        print(f"The latest version of {a} is {b}")

def main():
    parser = argparse.ArgumentParser(
        description='This script takes a image and either shows the latest version of the image or if the version is a valid version'
    )
    parser.add_argument('--lastupdated,','-i', dest='image', type=str,
                        help= "Please enter an image to get the last updated version")
    parser.add_argument('--version','-v', action='append', dest='version', type=str,
                        help= "Please enter a image then its version number ")
    parser.add_argument('--latestversion','-l', dest='latest', type=str,
                        help= "Please enter an image to get the lastest version ")

    args = parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    if args.image:
        versions = api(args.image)
        number = manipulate(versions)
        last_updated(args.image, number)
    if args.version:
        versions = api(args.latest)
        info = manipulate(versions)
        version_list(args.latest, info, args.version)
    if args.latest:
        versions = api(args.latest)
        number = manipulate (versions)
        last_version(args.latest,number)
if __name__ == '__main__':
    main()


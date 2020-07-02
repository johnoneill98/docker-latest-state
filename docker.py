"import statements"
from operator import itemgetter
import argparse
import sys
import requests


def validversion(vname):
    """[summary]
    This function takes the version number of an images and tells if its a valid version or not.
    If the version has words in ti then it is is valid

    Args:
        vname: the name of the version

    Returns:
        A boolean value that tells if the version number is valid or not based on
        if the version numbers has only numbers and decimals or not
    """
    isvalid = True
    for value in vname:
        if not (value.isnumeric() or value == "."):
            isvalid = False
            break
    return isvalid


def api(image):
    """[summary]
    User sumbits an image name and it will contact the api endpoint to retrive all the version
    information that docker supports
    Args:
        image from dockerHub

    Returns:
        a list of all version of the supported  images from dockerHub
    """
    # replaces all spaces with dashes to satisfy the api call
    user = image.replace(" ", "-")
    # complete api call
    if user.find("/") != -1:
        url = "https://registry.hub.docker.com/v2/repositories/"
    else:
        url = "https://registry.hub.docker.com/v2/repositories/library/"
    response = requests.get(f"{url}/{user}/tags?page=1&page_size=100")
    # Error checking
    if response.status_code != 200:
        print(f"Error {image} does not have any infomarion about version numbers")
        sys.exit()
    response = response.json()
    if response["results"] == []:
        print(f"Error{user}does not hae any information about version numbers")
    response = response["results"]
    return response


def manipulate(response):
    """[summary]
    Takes the input from the api call and manipulates it into a readable list

    Args:
        response ([list]): a list of all version for a image

    Raises:
        IndexError: If the user puts an incorrect image

    Returns:
        [list] returns all the images by earliest updated to latest updated
    """
    names = {}
    test = []
    for las in response:
        vname = las["name"]
        last_updated = las["last_updated"]
        test.append(last_updated)
        if last_updated is None:
            test.remove(last_updated)
        # formating the date for it to be easier to read
        last_updated = str(test).replace("T", " ")
        if validversion(vname):
            values = {last_updated: vname}
            names.update(values)
    # list of tuples from earliest and latest
    new_list = sorted(names.items(), key=lambda kv: (kv[1], kv[0]))
    # itemgetter takes the list of tuples  and returns every value at index 1 for each tuple
    new_list = list(map(itemgetter(1), new_list))
    if new_list == []:
        raise IndexError("image does not exist")
    return new_list


def last_version(versions):
    """
    Retrives a list of tuples and sorts the versiona from highest to lowest

    Args:
        versions ([list of tuples]): a list tuples from the manipulate function

    Returns:
        [str]: a string that is the latest version of an image
    """
    finallist = []
    for newversion in versions:
        versionnumberlist = newversion.split(".")
        actualnumber = 0.0
        for iterate, newplace in enumerate(versionnumberlist):
            actualnumber = actualnumber + (int(newplace) / (10 ** iterate))
        finallist.append((actualnumber, newversion))
    finallist.sort(reverse=True)
    return finallist[0][1]


def main():
    """
    The function will the read the command the arguments and will do the appropriate action
    """
    parser = argparse.ArgumentParser(
        description="This script takes a image and shows either the "
        "the latest version, the last version that was updated of the image"
        " or if the version is a valid version"
    )
    parser.add_argument(
        "image",
        type=str,
        help="please enter a image name like so 'python3 docker.py <imagename>'",
    )
    parser.add_argument(
        "-v",
        action="append",
        dest="version",
        type=str,
        help="Please enter a image then its version number like so"
        " 'python3 docker.py <imagename> -v <versionnumber>'",
    )
    parser.add_argument(
        "-l",
        action="store_true",
        help="Please enter '-l' to get the latest version like so "
        " 'python3 docker.py <imagename> -l'",
    )
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    versions = api(args.image)
    number = manipulate(versions)
    print(f"The version of {args.image} that was last updated is {number[-1]}")
    if args.version:
        value = args.version.pop()
        if value not in number:
            print(f"Version: {value} is not a valid version of  {args.image}")
            print(f"Valid versions of {args.image} are")
            print(f"{number}")
        else:
            print(f"Version {value} is a valid version of {args.image}")

    if args.l:
        latest = last_version(number)
        print(f"The latest version of {args.image} is {latest}")


if __name__ == "__main__":
    main()

import argparse
import requests
def validVersion(vname):
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
    #api call
    url = 'https://registry.hub.docker.com/v2/repositories/library/'
    #replaces all spaces with dashes to satisfy teh api call
    ui = image.replace(" ", "-")
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
    # list of tuples
    new_list=(sorted(names.items(), key = lambda kv: (kv[0], kv[1])))
    return new_list
def latest(image):
    versions = api(image)
    print(type(versions))
    print(versions[-1])
def version(image, number):
    versions = api(image)
    if number not in versions:
        print( "Version " + number + " is not accepted .Accepted versions are ")
        for item in versions:
            print (item ,"\n")

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

import argparse
import requests

def api(image):
    """This is a function that goes to the api endpoint and goes to the "full_description" tag to retrive information

    Args:
        an API image

    Returns:
    The full descrption of the api
    """
    url = "https://hub.docker.com/v2/repositories/library"
    # if the image name is twp name then all spaces becomes dashes
    try:
        print(image)
        ui = image.replace(" ", "-")
        response = requests.get(f"{url}/{ui}/")
        response = response.json()
        desc = response['full_description']
        desc = desc.split('\n')
        return desc
    except KeyError:
        print("Full Description is not in the field")

def main():
    parser = argparse.ArgumentParser(
        description='This script takes a image and either shows the latest version of the image or if the version is a valid version'
    )
    parser.print_help()
    parser.add_argument('--image', '-i', dest='image', type=str, required=True,
                        help="Please enter a image name.")

    parser.add_argument('--version', '-v', dest='version', type=str,
                        help="Please enter a version number to see if it is valid or not.")
    args = parser.parse_args()

    if args.image:
        try:
            args.image = args.image.lower()
            image = api(args.image)
            desc1 =list(filter(lambda x: 'latest' in x, image))
            desc1 = desc1[0].split(',')
            sDesc =(desc1[0].split('`')[1].split(desc1[0])[0])
            print("Latest version of " + args.image+ " is " + sDesc)
        except KeyError:
            print("Can not find image")
        except ValueError:
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
        except UnboundLocalError:
            print("You must put an image name first then the version number")
if __name__ == "__main__":
    main()

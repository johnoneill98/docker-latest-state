# This code is to test for how python accepts commandline arguments

import sys
import getopt
import api


def main(argv):
    inputfile = ''
    try:
        opt, args = getopt.getopt(argv, "hi:l s", ["ifile="])
    except getopt.GetoptError:
        print("If you need help, type 'python3 argument.py -h'")
        sys.exit(2)
    for opt, arg in opt:
        if opt == '-h':
            print("Correct formatting is 'python3 argument.py -i <imageName>' for looking up an image")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            api.search(inputfile)


if __name__ == "__main__":
    main(sys.argv[1:])

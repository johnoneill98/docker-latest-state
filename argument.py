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
            print("Correct formatting is 'python3 argument.py -l' for  a list of all known images ")
            print("Correct formatting is 'python3 argument.py -s' for  a sorted list of all known images ")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            api.search(inputfile)
        elif opt == ("-l"):
            api.list()
        elif opt == ("-s"):
            api.sortedList()


if __name__ == "__main__":
    main(sys.argv[1:])

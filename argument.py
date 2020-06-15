# This code is to test for how python accepts commandline arguments

import sys
import getopt
import api


def main(argv):
    inputfile = ''
    number = ''
    try:
        opt, args = getopt.getopt(argv, "hi:v:", ["ifile=","lfile=","number="])
    except getopt.GetoptError:
        print("If you need help, type 'python3 argument.py -h'")
        sys.exit(2)
    for opt, arg in opt:
        if opt == '-h':
            print("Correct formatting is 'python3 argument.py -i <imageName>' for looking up the latest version of an an image")
            print("Correct formatting is 'python3 argument.py -v <imageName> <imageNumber>' to see if a version of an image exists ")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            api.search(inputfile)
        elif opt in ("-v", "--lfile","--number"):
            name = arg
            number =args[0]
            api.printNumber(name, number)
if __name__ == "__main__":
    main(sys.argv[1:])

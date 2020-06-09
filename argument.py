# This code is to test for how python accepts commandline arguments

import sys, getopt
import api

def main(argv):
    inputfile =''
    try:
        opt, args = getopt.getopt(argv, "hi:l",["ifile="])
    except getopt.GetoptError:
        print ("If you need help, type 'python3 argument.py -h'")
        sys.exit(2)
    for opt, arg in opt:
      if opt == '-h':
         print("Correct formating is 'python3 argument.py -i <inputfile>' for looking up an image")
         print("Correct formating is 'python3 argument.py -l' for listing all known images ")
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         api.search(inputfile)
      elif opt == ("-l"):
          api.list()
if __name__ == "__main__":
   main(sys.argv[1:])

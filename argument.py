# This code is to test for how python accepts commandline arguments

import sys, getopt

def main(argv):
    inputfile =''
    outputfile = ''
    try:
        opt, args = getopt.getopt(argv, "hi:o",["ifile="])
    except getopt.GetoptError:
        print ("If you need help, type 'python argument.py -h'")
        sys.exit(2)
    for opt, arg in opt:
      if opt == '-h':
         print ("argument.py -i <inputfile> ")
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         print("this is a test")
    print ("Input file is", inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])

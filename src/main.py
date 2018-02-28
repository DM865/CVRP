#!/usr/bin/python3

import sys
import getopt
import os

import data


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ht:i:o:",["help","time_limit=","instance=","output_file="])
    except getopt.GetoptError:
        usage()
        sys.exit("Command line options missing")

    
    instance_file=""
    output_file=""
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()                     
            sys.exit(0)
        elif opt in ("-t", "--time_limit"): 
            time_limit = int(arg)
        elif opt in ("-o", "--output_file"): 
            output_file = arg        
        elif opt in ("-i", "--instance"): 
            instance_file = arg        


    instance = data.Data(instance_file)


    

def usage():
    print("\n")
    print("Usage: [--help, --instance=, --time_limit=, --output_file=]\n")




if __name__ == "__main__":
    main(sys.argv[1:])
